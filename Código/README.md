# Tabla de Contenido
1. [Preliminares](#Preliminares "Preliminares")
2. [Librerías](#Librerías "Librerías")
3. [Variables globales](#Variables-globales "Variables globales")
4. [Inicio del programa](#Inicio-del-programa "Inicio del programa")
5. [Función `main()`](#Función-main "Función main")

---

# Preliminares

El siguiente segmento de código será para no tener ninguna clase de problema con los acentos o caracteres especiales que se encuentren en el programa.

```python
{
    #La siguiente instrucción sirve para no tener problemas con los acentos o caracteres especiales del lenguaje natural.
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
}
```

# Librerías

La siguiente es la sección de importaciones de las librerías usadas en el programa. La librería `cv2` y `pyzbar` permitiran hacer la carpura de video en tiempo real con la cámara y el tratamiento de los códigos de barras respectivamente; por otro lado, la librería `remove` y `path` servirán para hacer la creación de un archivo nuevo cada vez que se inicie el programa.

```python
{
    #La siguiente librería permite hacer la lectura de códigos en tiempo real.
    import cv2
    #La librería a continuación permite hacer el tratamiento de los diferentes códigos de barras.
    from pyzbar import pyzbar
    from pyzbar.pyzbar import ZBarSymbol
    #Las siguientes librerías permiten ubicar y remover el archivo data.txt si existe previamente.
    from os import remove
    from os import path
}
```

# Variables globales

Se decide vincular la variable `NUM_BLOQUES` a diferentes segmentos del código con el fin de generar una posible ampliación de los códigos leídos por el programa, en este caso será igual a `2`, se recomienda que sea no superior a `4`.

```python
{
    #Variable vinculada al número de bloques que se espera leer en el programa, se recomienda no superior a 4.
    NUM_BLOQUES = 2
}
```

# Inicio del programa 

Este se da con la instrucción que busca la función `main()` en el archivo para poder ejecutarla.

```python
{
    #Instrucción principal para la ejecución del programa con la función main()
    if __name__ == '__main__':
        main()
}
```

# Función `main()`

Lo principal es la función `main()`, la cual contiene:

1. Una instrucción para **borrar** en caso de que exista, el archivo **data.txt** que será el que almacena la posición de los códigos de barras como salida del programa.

```python
{
    #Verifica si existe el archivo data.txt y de ser así lo borra.
    if path.exists("data.txt"):
        remove('data.txt')
}
```

2. La creación de la instancia de la clase `Captura_codigos` que será la que contenga el resto del programa, siguiente de ella se tiene una línea que especifica la fuente de video que va a detectar el programa; en este caso se usa `2` debido a que corresponde a la activación de la cámara conectada al puerto USB, sin embargo, **se debe configurar cambiando los números desde el 0 hasta que se de la orden de activación de la cámara donde se quiere implementar el programa**. Por último, se toman los parámetros de lectura de la cámara.

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

3. Se tiene a continuación un ciclo que se ejecuta mientras la cámara sea reconocida; este ciclo hace posible la actualización del marco de captura de video. Si se quiere detener la captura de video y detener el programa será necesario precionar la tecla **ESC**, esta tecla puede ser cambiada en la instrucción del condicional cambiando el `0xFF == 27` por el indicativo de la tecla de preferencia.

```python
{
    #Ciclo que se ejecuta mientras la cámara esté disponible y solo se detiene al presionar la tecla ESC.
    while ret:
        ret, frame = camera.read()
        frame = Capturar.read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        #Condicional para leer la tecla ESC y abandonar el programa.
        if cv2.waitKey(1) & 0xFF == 27:
            break
}
```

4. Al finalizar la ejecución del programa se detiene la captura y se destruyen todas las ventanas.

```python
{
    #Se finaliza la lectura de la cámara.
    camera.release()
    #Se destruyen todas las ventanas creadas.
    cv2.destroyAllWindows()
}
```
