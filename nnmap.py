from threading import Thread
import socket
from ipaddress import IPv4Address
from platform import uname
from os import system
from time import sleep

if list(uname())[0] == 'Windows':
    system("chcp 65001")
    system("cls")
else:
    print("try windows 7 host for colouring")
while True:
    try:
        dig = input("Fuck yo ip: ")
        h = ipaddress.IPv4Address(dig)
        break
    except Exception as hr:
        print("jive ip u moron")
opens = []
def f(ite):
    ite.sort()
    print(f"{len(ite)} psorts are online")
    print()
    for i in ite:
        print(f"\033[92m[+] Posrt {i} is open")
def sex(a):
    for i in range(a[0], a[1]):
        g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        g.settimeout(0.01)
        ff = g.connect_ex((dig, i))
        if ff == 0:
            opens.append(i)
        g.close()
def guu():
    m = [i for i in range(1, 50002, 250)]
    for i in range(200):
        sexx = threading.Thread(target=sex, args=(m[i:i+2],))
        sexx.start()
if __name__ == "__main__":
    guu()
# iha par gadbad che, thikh kardije ga
    sleep(4)    
    print()
    f(opens)
    print("\n if all ports no looking ten, try increze time nd chek wit nmap")
