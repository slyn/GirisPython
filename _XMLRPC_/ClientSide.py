import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.mod(10,3))  # Sonuc 10 % 3 = 1
print(s.topla(2,3))  # Sonuc 3 + 2 = 5
print(s.cikar(5,2))  # Sonuc 5 - 2 = 3
print(s.us(3,2))  # Sonuc 3 ^ 2 = 9

print(s.system.listMethods())

