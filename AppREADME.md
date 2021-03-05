Lo principal es la función ***main()***, la cual contiene:

1. Una instrucción para ***borrar*** en caso de que exista, el archivo data.txt que será el que almacena la posición de los códigos de barras como salida del programa.

```python
{
    #Verifica si existe el archivo data.txt y de ser así lo borra.
    if path.exists("data.txt"):
        remove('data.txt')
}
```

2. La creación de la instancia de la clase `Captura_codigos` que será la que contenga el resto del programa, siguiente de ella se tiene una línea que especifica la fuente de video que va a detectar el programa; en este caso se usa `2` debido a que corresponde a la activación de la cámara conectada al puerto USB, sin embargo, se debe configurar cambiando los números desde el 0 hasta que se de la orden de activación de la cámara donde se quiere implementar el programa; por último, se toman los parámetros de lectura de la cámara.

```python
{
    #Instancia de la clase Captura_codigos
    Capturar = Captura_codigos()
    '''Orden de activación a la cámara, el número 2 puede variar desde 0
    depende la fuente de video.'''
    camera = cv2.VideoCapture(2)
    #Captura de parámetros de la cámara.
    ret, frame = camera.read()
}
```
