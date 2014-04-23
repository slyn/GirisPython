import random
global tahmin_sayisi


def tahmin_et():
    while True:
        tahmin = int(input('TAHMININIZ...: '))
        if 0 <= tahmin <= 100:
            return tahmin
        else:
            print('Gecersiz Tahmin')


def tahmin_baslasin():
    a = True
    sayi = random.randint(0, 100)
    # print(sayi)
    while a:
        print('0 ile 100 Arasinda bir tahmin yapin' )
        b = tahmin_et()
        if b == sayi:
            print('Sayiyi Dogru Tahmin ettiniz')
            a = False
        elif b > sayi:
            print('Tahmininiz buyuk')
        else:
            print('Tahmininiz kucuk')

tahmin_baslasin()
