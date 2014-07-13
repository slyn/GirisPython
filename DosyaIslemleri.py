#!/usr/bin/env python

'''Dosya acma formati 
f=open('Dosya adi','dosya acma modu')
Dosya acma modlari
a,ab,ab+,r,rb,rb+,w,wb,wb+
'''

#Yazilmak uzere yeni dosya acmak
dosya = open('/root/Desktop/dosyam.txt','w')

#Acilan dosyaya yazi yazmak
dosya.write('...DOSYAMA YAZIYORUM...\n ')
dosya.write('!!! 2.SATIRDAYIM !!!')

#Dosyayi kapatmak
dosya.close()

#--------------------

#Var olan dosyayi sadece okumak icin acmak
dosya = open('/root/Desktop/dosyam.txt','r')

#Dosyadan okumak icin
#print(dosya.read())
dosyadan = dosya.readlines()

for satirlar in dosyadan:
	print(satirlar)

dosya.close()

#-------------------

#Otomatik kapanan dosya
#bir blok olusturulur ve blok icersinde dosya islemleri yapilir islem sonunda dosyanin kapatilmasina gerek yoktur
with open('/root/Desktop/dosyam.txt','a+') as dosyadan:
	dosyadan.write('\nPamukkale Universitesi \n')
	dosyadan.write('Denizli')

	#Dosya imlecini dosyanin sonundan basina tasimak icin seek fonksiyonu kullanilir.
	dosyadan.seek(0)
	#imlecin bulundugu yeri ogrenmek icin tell() metodu kullanilir

	veri = dosyadan.readlines()

	for satirlar in veri:
		print(satirlar)
