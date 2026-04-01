"""Notebook watcher — polling-based auto-analysis for new/changed notebooks."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import TextIO

from .notebook_analysis import build_notebook_analysis
from .storage import RegistryPaths


def watch_notebooks(
    paths: RegistryPaths,
    watch_dir: Path,
    *,
    interval_seconds: int = 60,
    auto_propose: bool = True,
    out: TextIO | None = None,
) -> None:
    """Poll watch_dir for new/changed .ipynb files and auto-analyze them."""
    import sys
    out = out or sys.stdout
    hash_file = paths.root / ".notebook_hashes.json"
    known_hashes = _load_hashes(hash_file)

    out.write(f"Watching {watch_dir} (interval={interval_seconds}s, auto_propose={auto_propose})\n")
    out.flush()

    try:
        while True:
            changed = _scan_for_changes(watch_dir, known_hashes)
            for notebook_path in changed:
                out.write(f"\nAnalyzing: {notebook_path.name}\n")
                out.flush()
                try:
                    result = build_notebook_analysis(str(notebook_path), spec="auto")
                    out.write(f"  Spec: {result.spec_slug}\n")
                    out.write(f"  Tickers: {len(result.analyses)}\n")
                    out.write(f"  Unresolved: {len(result.unresolved_items)}\n")
                    out.write(f"  Themes: {len(result.themes)}\n")
                    out.write(f"  Indicators: {len(result.indicators)}\n")

                    if auto_propose:
                        from .semantic_inference import infer_notebook_semantics
                        from .llm import build_llm_client_from_env
                        try:
                            llm = build_llm_client_from_env()
                            proposals = infer_notebook_semantics(paths, str(notebook_path), llm_client=llm)
                            out.write(f"  Proposals generated: {len(proposals.proposals)}\n")
                        except Exception as e:
                            out.write(f"  Proposals skipped: {e}\n")

                    known_hashes[str(notebook_path)] = _file_hash(notebook_path)
                except ValueError as e:
                    out.write(f"  Skipped: {e}\n")
                    known_hashes[str(notebook_path)] = _file_hash(notebook_path)
                out.flush()

            _save_hashes(hash_file, known_hashes)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        out.write("\nWatcher stopped.\n")
        _save_hashes(hash_file, known_hashes)


def _scan_for_changes(watch_dir: Path, known_hashes: dict[str, str]) -> list[Path]:
    """Return list of .ipynb files that are new or changed since last scan."""
    changed = []
    for notebook_path in sorted(watch_dir.glob("*.ipynb")):
        current_hash = _file_hash(notebook_path)
        if known_hashes.get(str(notebook_path)) != current_hash:
            changed.append(notebook_path)
    return changed


def _file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _load_hashes(path: Path) -> dict[str, str]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def _save_hashes(path: Path, hashes: dict[str, str]) -> None:
    path.write_text(json.dumps(hashes, indent=2), encoding="utf-8")
