#!/usr/bin/python3.4
import os

# isletim sistemi belirlemek icin
c = os.name
print('----')
if c == 'posix':
	print('Isletim Sisteminiz ...: LINUX')
#	os.system('ps -aux')
elif c is 'dos' or 'ce' or 'nt' :
	print('Isletim Sisteminiz ...: WINDOWS')
elif c is 'mac':
	print('Isletim Sisteminiz ...: MACINTOSH')
elif c is 'os2':
	print("Isletim Sisteminiz ...: OS/2")
elif c is  'riscos':
	print('Isletim Sisteminiz ...: Risc OS')
else:
	print('Isletim Sisteminiz ...: TESPIT EDILEMEDI')

print('----')
print('ps -aux')
print('--')
if c == 'posix':
	os.system('ps -aux')
	print('Linux komutu CALISITIRILDI...!')
else:
	print('CALISITIRILMADI...!')
