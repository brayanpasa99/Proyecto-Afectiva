# Proyecto Afectiva - Colaboración Grupo VIRTUS

> Brayan Alexander Paredes Sánchez

# Carpeta [Generación Códigos](https://github.com/brayanpasa99/Proyecto-Afectiva/tree/main/Generaci%C3%B3n%20c%C3%B3digos)

En esta carpeta se encuentra un [archivo .zip](https://github.com/brayanpasa99/Proyecto-Afectiva/blob/main/Generaci%C3%B3n%20c%C3%B3digos/barcodes.zip) que contiene los códigos generados en la plataforma [Online Barcode Generator](https://barcode.tec-it.com/es).

También, se encuentra un [archivo .docx](https://github.com/brayanpasa99/Proyecto-Afectiva/blob/main/Generaci%C3%B3n%20c%C3%B3digos/Codigos1a10.docx) que fue el de referencia para hacer la impresión de los códigos en los diferentes tamaños usados. Se tiene que las primeras tres líneas del archivo son las que presentan mejores resultados, siendo la primera la usada en las pruebas hasta el momento.

Igualmente, encontrará cada uno de los enlaces a las diferentes imágenes de los códigos de barras.

# Archivo App.py

Este será el principal del proyecto y contiene el código usado para la implementación del mismo, se explica este más a fondo:

Lo principal es la función ***main()***, la cual contiene:

1. Una instrucción para ***borrar*** en caso de que exista, el archivo data.txt que será el que almacena la posición de los códigos de barras como salida del programa.

```python
{
    if path.exists("data.txt"):
        remove('data.txt')
}
```

2. La creación de la instancia de la clase ***Captura_codigos*** que será la que contenga el resto del programa, siguiente de ella se tiene una línea que especifica la fuente de video que va a detectar el programa; en este caso se usa 2 debido a que corresponde a la activación de la cámara conectada al puerto USB, sin embargo, se debe configurar cambiando los números desde el 0 hasta que se de la orden de activación de la cámara donde se quiere implementar el programa; por último, se toman los parámetros de lectura de la cámara.

```python
{
    Capturar = Captura_codigos()
    camera = cv2.VideoCapture(2)
    ret, frame = camera.read()
}
```
