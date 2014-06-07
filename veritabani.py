
import sqlite3


#baglanti kurmak icin
c=sqlite3.connect('veritabim.db')


#bos veritabanina tablo olusturmak icin
c.execute('''create table kisilerim
(id int primary key not null,
ad text not null,
yas int not null)''')


#var olan tabloya veri girmek icin
c.execute("insert into kisilerim (id, ad, yas) values (1, 'husnu', 22)")


#var olan tabloda veri guncellemekicin
c.execute("update kisilerim set ad = 'hüsnü' where id = 1")


c.execute('insert into kisilerim (id, ad, yas) values (2, "slyn", 22')
#var olan kaydi veri tabanindan silmek
c.execute('delete from kisilerim where id = 2')


#kayitlari ekranda gostermek icin
for i in c.execute('select * from kisilerim'):
  print(i)
  
