#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
# Importa el modulo socketserver.
import socketserver
import sys

#Claase que manejara las peticiones. Clase hereda de DatagramaRequestHandler.
class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    # Metodo que se ejecuta cada vez que recibimos una peticion.
    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        cliente_info = self.client_address
        print (cliente_info[0])
        print (cliente_info[1])
        while 1:
            line = self.rfile.read()

#Tratamos como un fichero; self.wfile y self.rfile.

if __name__ == "__main__":
    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
