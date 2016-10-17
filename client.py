#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""
# Importa el modulo socket.
import socket

# Constantes. Dirección IP del servidor y contenido a enviar.
SERVER = 'localhost'
PORT = 6001
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
# Send para enviar y recv para recibir. Ademas el buffer de recv en bytes.

# El socket deja de existir cuando acaba el with no hace falta cerrarlo.
# b linea 18: bytes, si fuera u seria en utf.

print("Socket terminado.")
