"""Qwen bağlantı testi — terminalde: python test_qwen.py"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url=os.getenv("QWEN_BASE_URL"),
)


def sor(soru: str) -> str:
    yanit = client.chat.completions.create(
        model=os.getenv("QWEN_MODEL", "qwen-turbo"),
        messages=[
            {
                "role": "system",
                "content": "Sen Türkiye ekonomisi konusunda uzman bir analistsin. Kısa ve net yanıt ver.",
            },
            {"role": "user", "content": soru},
        ],
    )
    return yanit.choices[0].message.content


if __name__ == "__main__":
    print("Qwen bağlantısı test ediliyor...\n")

    sorular = [
        "Cari açık nedir, 2 cümleyle açıkla.",
        "Türkiye'de çekirdek enflasyon hangi kalemleri dışarıda bırakır?",
    ]

    for soru in sorular:
        print(f"SORU: {soru}")
        print(f"YANIT: {sor(soru)}")
        print("-" * 60)
