#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('Slice.ice')
import IceGauntlet

class Client(Ice.Application):
    
    def getMap(self):
        archivo = open("client_maps/mapa_descargado.json","w")
        archivo.write(self.room.getRoom())
        archivo.close()

    def publishMap(self):
        print()
        while(true):
            try:
                new_room=open("client_maps/"+input(), "r")
                break
                
            except FileNotFoundError:
                print("Archivo no encontrado")

        self.room.publish(new_room)

    def removeMap():
        print()

    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        self.room = IceGauntlet.RoomPrx.checkedCast(proxy)

        if not self.room:
            raise RuntimeError('Invalid proxy')
        
        option=-1
        while option <0 or option>5:
            try:
                print("Elige una opción: \n  [1] Obtener un mapa. \n  [2] Subir mapa. \n  [3] Borrar un mapa. \n  [0] Salir")
                option=int(input())
            except ValueError:
                print("Tiene que ser un numero")

        if option==1:
            self.getMap()
        elif option==2:
            self.publishMap()
        elif option==3:
            self.removeMap()

        print("Adiós.")
        
        return 0


sys.exit(Client().main(sys.argv))