import zbar
import numpy as np
import cv2
 
#Inicializar la camara 0 para la camara del portatil y 1 para la webcam
capture = cv2.VideoCapture(2)
 
while 1:
    #Capturar un frame
    val, frame = capture.read()
 
    if val:
        #Capturar un frame con la camara y guardar sus dimensiones
        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dimensiones = frame_gris.shape #'dimensiones' sera un array que contendra el alto, el ancho y los canales de la imagen en este orden.
 
        #Convertir la imagen de OpenCV a una imagen que la libreria ZBAR pueda entender
        imagen_zbar = zbar.Image(dimensiones[1], dimensiones[0], 'Y800', frame_gris.tobytes())
 
        #Construir un objeto de tipo scaner, que permitira escanear la imagen en busca de codigos QR
        escaner = zbar.ImageScanner()
 
        #Escanear la imagen y guardar todos los codigos QR que se encuentren
        escaner.scan(imagen_zbar)
 
        for codigo_qr in imagen_zbar:
            dat = codigo_qr.data[:-2] #Guardar el mensaje del codigo QR. Los ultimos dos caracteres son saltos de linea que hay que eliminar
            print(dat)
 
        #Mostrar la imagen
        cv2.imshow('Imagen', frame)
 
    #Salir con 'ESC'
    if cv2.waitKey(1) & 0xFF == 27:
        break

    #if cv2.waitKey(5) & 0xFF == 27:
        #break
 
 
 
cv2.destroyAllWindows()