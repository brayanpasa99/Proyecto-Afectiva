#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
import operator
from os import remove
from os import path

NUM_BLOQUES = 2

class Captura_codigos:
    
    def __init__(self):
        self.dato_coordenada={}
        self.initial_positions={}
        self.current_positions={}
        self.cadena=""

    def read_barcodes(self, frame):
        barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])
        self.dato_coordenada={}
        for barcode in barcodes:
            x, y, w, h = barcode.rect      
            barcode_text = barcode.data.decode('utf-8')      
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)   
            self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)

        if(len(self.dato_coordenada)>0 and len(self.dato_coordenada)==NUM_BLOQUES):
            self.ordena(self.dato_coordenada)

        return frame

    def ordena(self, coor): 
        coor_x = {}
        coor_y = {}

        for key in coor:
            coor_x[key]=coor[key][0]
            coor_y[key]=coor[key][1]

        valores = coor_x.values()
        llaves = coor_x.keys()

        ordenados = self.selectionSort(valores, llaves)

        nueva_cadena = ""

        for i in range(len(ordenados[1])):
            nueva_cadena = nueva_cadena +" "+ str(ordenados[1][i])
        
        if(nueva_cadena==self.cadena):
            pass
        else:
            self.cadena = nueva_cadena
            self.appendText(self.cadena)

    def selectionSort(self, vList, llList):
        for i in range(len(vList)):
            least = i
            for k in range(i+1, len(vList)):
                if vList[k] < vList[least]:
                    least = k
                    
            self.swap(vList, llList, least, i)

            return [vList, llList]
            
    def swap(self, V, LL, x, y):
        temp = [V[x], LL[x]]
        [V[x], LL[x]] = [V[y], LL[y]]
        [V[y], LL[y]] = temp

    def appendText(self, cadena):

        f = open('data.txt','a')
        f.write('\n' + cadena)
        f.close()

def main():

    #Verifica si existe el archivo data.txt y de ser así lo borra.
    if path.exists("data.txt"):
        remove('data.txt')

    #Instancia de la clase Captura_codigos
    Capturar = Captura_codigos()
    '''Orden de activación a la cámara, el número 2 puede variar desde 0
    depende la fuente de video.'''
    camera = cv2.VideoCapture(2)
    #Captura de parámetros de la cámara.
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = Capturar.read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()