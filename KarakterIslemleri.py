karakter_dizi = 'Python Programlama Dili'

print('TERSTEN: \n ', karakter_dizi[::-1])
#iliD amalmargorP nohtyP

print('ILK 5 KARAKTERDEN SONRASI : \n ', karakter_dizi[6:])
#Programlama Dili

print('TEK INDEX NUMARALARINDA OLANLAR : \n ', karakter_dizi[1::2])
#yhnPormaaDl

print('CIFT INDEX NUMARALARINDA OLANLAR: \n ', karakter_dizi[0::2])
#Pto rgalm ii

print('SON 5 KARAKTERDEN ONCESI : \n ', karakter_dizi[:-5])
#Python Programlama

print(karakter_dizi.split())
#['Python', 'Programlama', 'Dili']
manav_listesi='Elma,Armut,Ananas,Portakal,Muz,Kivi'
print(manav_listesi)
#Elma,Armut,Ananas,Portakal,Muz,Kivi
print(manav_listesi.split(','))
#['Elma', 'Armut', 'Ananas', 'Portakal', 'Muz', 'Kivi']

print(*karakter_dizi)
#P y t h o n   P r o g r a m l a m a   D i l i

print(*karakter_dizi, sep='.')
#P.y.t.h.o.n. .P.r.o.g.r.a.m.l.a.m.a. .D.i.l.i

print('IZMIR', 'DENIZLI', 'BURDUR', sep='-')
#IZMIR-DENIZLI-BURDUR

print(karakter_dizi)
print(karakter_dizi.capitalize())
#Python Programlama Dili
#Python programlama dili

print(str.lower('DeNiZLi'))
#denizli
print(str.capitalize('DeNiZLi'))
#Denizli
print(str.upper('DeNiZLi'))
#DENIZLI

print('{0} {1} {2}'.format('Ali', 'Veli', 'Mehmet'))
#Ali Veli Mehmet
print('{2} {1} {0}'.format('Ali', 'Veli', 'Mehmet'))
#Mehmet Veli Ali
print('{} {} {}'.format('Ali', 'Veli', 'Mehmet'))
#Ali Veli Mehmet
print('{0} {0} {0}'.format('Ali', 'Veli', 'Mehmet'))
#Ali Ali Ali


