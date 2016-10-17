#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
# Importa el modulo socketserver.
import socketserver

#Claase que manejara las peticiones. Clase hereda de DatagramaRequestHandler.
class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    # Metodo que se ejecuta cada vez que recibimos una peticion.
    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))
#Tratamos como un fichero; self.wfile y self.rfile.

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
