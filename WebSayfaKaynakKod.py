
#url adresi girilen sitenin kaynak kodu ismi girilen dosyaya kaydedilir
from urllib.request import urlretrieve


def site_al():
    return str(input('Kaynak Koduna Erisilecek Site: '))


def adi():
    return str(input('Dosya Adini Gir: '))


url = site_al()
file_name = adi()
urlretrieve(url, file_name)
