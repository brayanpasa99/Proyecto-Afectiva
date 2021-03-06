#!/usr/bin/env python
# -*- coding: utf-8 -*-

#La siguiente librería permite hacer la lectura de códigos en tiempo real.
import cv2
#La librería a continuación permite hacer el tratamiento de los diferentes códigos de barras.
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
#Las siguientes librerías permiten ubicar y remover el archivo data.txt si existe previamente.
from os import remove
from os import path

#Variable vinculada al número de bloques que se espera leer en el programa, se recomienda no superior a 4.
NUM_BLOQUES = 2

class Captura_codigos:
    
    #Se define el constructor o clase fundamental con los atributos que tendrán las instancias de la clase.
    def __init__(self):
        self.dato_coordenada={}
        self.cadena=""

    #Función que se encarga de leer los códigos de barras, recibe el marco o la captura de la pantalla actual
    def read_barcodes(self, frame):
        #Variable que almacena los códigos de barras según los parámetros recibidos.
        barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])
        #Se limpia el diccionario de los datos de las coordenadas.
        self.dato_coordenada={}
        #Ciclo para recorrer todos los códigos de barras encontrados.
        for barcode in barcodes:
            #Se extraen las coordenadas del rectángulo decodificado en cada código para su futuro procesamiento.
            x, y, w, h = barcode.rect      
            #Se obtiene el dato leído en el código de barras y se almacena en una variable.
            barcode_text = barcode.data.decode('utf-8')      
            #Se definen las coordenadas, el color y el grosor (en pixeles) de la línea del rectángulo que se muestra 
            #en pantalla.
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)   
            #Se agregan los datos al diccionario considerando la llave como el código leído y las coordenadas x y y
            #como los datos asociados.
            self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)

        #Condicional para verificar que el arreglo contenga datos y a su vez estos datos sean igual al número de bloques
        #esperado, si esto se cumple, se envía el diccionario a la función de ordenamiento.
        if(len(self.dato_coordenada)>0 and len(self.dato_coordenada)==NUM_BLOQUES):
            self.ordena(self.dato_coordenada)

        #Se hace un retorno del marco actual.
        return frame

    #Se define la función que ordena el las coordenadas de los bloques.
    def ordena(self, coor):
        #Se inicializa un diccionario que va a contener las coordenadas en x del diccionario recibido. 
        coor_x = {}

        #Se construye un arreglo que va a recorrer el diccionario obtenido, asignando el valor como clave
        #el valor de la clave del diccionario principal y como dato asociado el valor de coordenada en x respectivo.
        for key in coor:
            coor_x[key]=coor[key][0]

        #El diccionario de coordenadas se divide en dos arreglos para el ordenamiento que contienen los valores
        #separados de las claves para que sea más fácil ordenarlos.
        valores = coor_x.values()
        llaves = coor_x.keys()

        #Se acude a la función que contiene el algoritmo para ordenar, enviando las claves
        #y los valores correspondientes a ser ordenados.
        ordenados = self.selectionSort(valores, llaves)

        #Se inicializa una nueva cadena que contiene la instrucción que se escribirá en el archivo posteriormente.
        nueva_cadena = ""

        #Se inicia un ciclo para construir la cadena que se va a imprimir en el archivo
        #se obtienen cada una de las claves que serán concatenadas en una única cadena de texto
        for i in range(len(ordenados[1])):
            nueva_cadena = nueva_cadena +str(ordenados[1][i])+" "
        
        '''Se compara la cadena almacenada en el atributo de la instancia y la cadena construida en la función
        si son iguales no se hace ningún proceso, si son diferentes se cambia la cadena de la instancia por
        la cadena de la función y además se llama a la función que añade el texto al archivo existente.'''
        if(nueva_cadena==self.cadena):
            pass
        else:
            self.cadena = nueva_cadena
            self.appendText(self.cadena)

    #Función que contiene el algoritmo de ordenamiento
    def selectionSort(self, vList, llList):
        #Proceso iterativo sobre el arreglo de valores
        for i in range(len(vList)):
            #Asignación de índice a comparar
            least = i
            #Proceso iterativo para la verificación con los demás datos del arreglo
            for k in range(i+1, len(vList)):
                #Comparación con los siguientes datos y guardar el índice en caso de que se encuentre un dato menor
                if vList[k] < vList[least]:
                    least = k
                    
            '''Llamado a la función con los arreglos de valores y llaves, además, con las posiciones para hacer los
            respectivos cambios'''
            self.swap(vList, llList, least, i)

            #Retorno de los arreglos ordenados
            return [vList, llList]

    #Función que permite hacer los cambios respectivos en los arreglos de llaves y valores.        
    def swap(self, V, LL, x, y):
        #Asignación de un dato temporal para hacer el cambio
        temp = [V[x], LL[x]]
        #Se hace el cambio correspondiente
        [V[x], LL[x]] = [V[y], LL[y]]
        #Se devuelven los valores a su posición correcta
        [V[y], LL[y]] = temp

    #Función para añadir los datos de la cadena al archivo
    def appendText(self, cadena):
        #Abrir el archivo en formato 'a' para añadir líneas sobre el archivo existente
        f = open('Codigo/data.txt','a')
        #Escribir la cadena en el archivo con un salto de línea
        f.write('\n' + cadena)
        #Cerrar el archivo
        f.close()

#Función principal
def main():

    #Verifica si existe el archivo data.txt y de ser así lo borra.
    if path.exists("Codigo/data.txt"):
        remove('Codigo/data.txt')

    #Instancia de la clase Captura_codigos
    Capturar = Captura_codigos()
    '''Orden de activación a la cámara, el número 2 puede variar desde 0
    depende la fuente de video.'''
    camera = cv2.VideoCapture(2)
    #Captura de parámetros de la cámara.
    ret, frame = camera.read()
    #Ciclo que se ejecuta mientras la cámara esté disponible y solo se detiene al presionar la tecla ESC.
    while ret:
        ret, frame = camera.read()
        frame = Capturar.read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        #Condicional para leer la tecla ESC y abandonar el programa.
        if cv2.waitKey(1) & 0xFF == 27:
            break

    #Se finaliza la lectura de la cámara.
    camera.release()
    #Se destruyen todas las ventanas creadas.
    cv2.destroyAllWindows()

#Instrucción principal para la ejecución del programa con la función main()
if __name__ == '__main__':
    main()