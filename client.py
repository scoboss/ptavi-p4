#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""
# Aclaraciones ejercicio 2.
# Importa el modulo socket.
import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar.
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
LINE_LISTA = sys.argv[3:]
LINE = ' '.join(LINE_LISTA)

if (LINE.split()[0] == 'register'):
        LINE = 'REGISTER' + 'sip' + LINE.split()[1] + 'SIP/2.0\r\n\r\n'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto.
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
# Send para enviar y recv para recibir. Ademas el buffer de recv en bytes.

# El socket deja de existir cuando acaba el with no hace falta cerrarlo.
# b linea 18: bytes, si fuera u seria en utf.

print("Socket terminado.")
