#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
# Importa el modulo socketserver.
import socketserver
import sys

#Claase que manejara las peticiones. Clase hereda de DatagramaRequestHandler.
class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    dicc = {}

    # Metodo que se ejecuta cada vez que recibimos una peticion.
    def handle(self):
        cliente_info = self.client_address
        print (cliente_info[0])
        print str(cliente_info[1])
        while 1:
            line = self.rfile.read()
            line_decod = line.decode('utf-8')
            if (len(line_decod) >= 2):
                if (line_decod.split()[0].upper() == 'REGISTER'):
                    if (line_decod.split()[1].endswith('.es')
                        or line_decod.split89[1].endswith('.com')
                            self.dicc[line_decod.split()[1]] = client_info[0]
                    print (self.dicc)
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                else:
                    self.wfile.write(b"Hemos recibido tu peticion\r\n")
                    print("El cliente nos manda:" + line_decod)
            else:
                self.wfile.write(b"Hemos recibido tu peticion\r\n")
                print("El cliente nos manda:" + line_decod)

            if not line:

    PORT = int(sys.argv[1])
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
