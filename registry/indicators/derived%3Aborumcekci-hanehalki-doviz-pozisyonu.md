---
record_type: indicator
id: derived:borumcekci-hanehalki-doviz-pozisyonu
title: Borumcekci'ye gore hanehalkinin doviz pozisyonu
status: approved
input_ids:
- evds:TP.HPBITABLO4.3
- evds:TP.EBONDPIYDEG.S14
- evds:TP.YDOSBAPIYDEG.S15
- evds:TP.YDOSBAPIYDEG.S34
- evds:TP.YDOSBAPIYDEG.S53
- evds:TP.YDOSBAPIYDEG.S72
formula_expression: evds:TP.HPBITABLO4.3 + evds:TP.EBONDPIYDEG.S14 + evds:TP.YDOSBAPIYDEG.S15
  + evds:TP.YDOSBAPIYDEG.S34 + evds:TP.YDOSBAPIYDEG.S53 + evds:TP.YDOSBAPIYDEG.S72
formula_description: Yurt ici yerlesik gercek kisilerin YP mevduati ile gercek kisilerin
  portfoyunde bulunan eurobond ve YP cinsi banka ve ozel sektor tahvillerinin toplami.
output_frequency: weekly
output_unit: Milyon ABD Dolari
economic_meaning: Hanehalkinin mevduat ve secilmis menkul kiymet bacaklari uzerinden
  izlenen brut doviz varlik stoku proxy gostergesidir.
validation_note: Net pozisyon degildir; yukumluluk ayagini icermez. Seri secimi Borumcekci
  tanimina dayanir.
theme_ids:
- theme:hanehalki-doviz-varliklari
body: '# Borumcekci''ye gore hanehalkinin doviz pozisyonu


  ## Formul

  evds:TP.HPBITABLO4.3 + evds:TP.EBONDPIYDEG.S14 + evds:TP.YDOSBAPIYDEG.S15 + evds:TP.YDOSBAPIYDEG.S34
  + evds:TP.YDOSBAPIYDEG.S53 + evds:TP.YDOSBAPIYDEG.S72


  ## Formul Aciklamasi

  Yurt ici yerlesik gercek kisilerin YP mevduati ile gercek kisilerin portfoyunde
  bulunan eurobond ve YP cinsi banka ve ozel sektor tahvillerinin toplami.


  ## Ekonomik Anlam

  Hanehalkinin mevduat ve secilmis menkul kiymet bacaklari uzerinden izlenen brut
  doviz varlik stoku proxy gostergesidir.


  ## Dogrulama Notu

  Net pozisyon degildir; yukumluluk ayagini icermez. Seri secimi Borumcekci tanimina
  dayanir.

  '
path: C:\Users\bthkr\OneDrive\Masaüstü\İş Kodlama\İş Agentı\drafts\derived%3Aborumcekci-hanehalki-doviz-pozisyonu.md
---
# Borumcekci'ye gore hanehalkinin doviz pozisyonu

## Formul
evds:TP.HPBITABLO4.3 + evds:TP.EBONDPIYDEG.S14 + evds:TP.YDOSBAPIYDEG.S15 + evds:TP.YDOSBAPIYDEG.S34 + evds:TP.YDOSBAPIYDEG.S53 + evds:TP.YDOSBAPIYDEG.S72

## Formul Aciklamasi
Yurt ici yerlesik gercek kisilerin YP mevduati ile gercek kisilerin portfoyunde bulunan eurobond ve YP cinsi banka ve ozel sektor tahvillerinin toplami.

## Ekonomik Anlam
Hanehalkinin mevduat ve secilmis menkul kiymet bacaklari uzerinden izlenen brut doviz varlik stoku proxy gostergesidir.

## Dogrulama Notu
Net pozisyon degildir; yukumluluk ayagini icermez. Seri secimi Borumcekci tanimina dayanir.
