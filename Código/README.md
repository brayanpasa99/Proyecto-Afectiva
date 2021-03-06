# Proyecto Afectiva - Colaboración Grupo VIRTUS
> Brayan Alexander Paredes Sánchez

## Documentación código

---

## Tabla de Contenido
### 1. [Preliminares](#Preliminares "Preliminares")
### 2. [Librerías](#Librerías "Librerías")
### 3. [Variables globales](#Variables-globales "Variables globales")
### 4. [Inicio del programa](#Inicio-del-programa "Inicio del programa")
### 5. [Función `main()`](#Función-main "Función main")
### 6. [Clase `Captura_codigos`](#Clase-Captura_codigos "Captura códigos")
###     a. [Función `read_barcodes(self, frame)`](#Función-read_barcodesself-frame "Función read_barcodes")

---

## Preliminares

El siguiente segmento de código será para no tener ninguna clase de problema con los acentos o caracteres especiales que se encuentren en el programa.

```python
{
    #La siguiente instrucción sirve para no tener problemas con los acentos o caracteres especiales del lenguaje natural.
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
}
```

## Librerías

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

## Variables globales

Se decide vincular la variable `NUM_BLOQUES` a diferentes segmentos del código con el fin de generar una posible ampliación de los códigos leídos por el programa, en este caso será igual a `2`, se recomienda que sea no superior a `4`.

```python
{
    #Variable vinculada al número de bloques que se espera leer en el programa, se recomienda no superior a 4.
    NUM_BLOQUES = 2
}
```

## Inicio del programa 

Este se da con la instrucción que busca la función `main()` en el archivo para poder ejecutarla.

```python
{
    #Instrucción principal para la ejecución del programa con la función main()
    if __name__ == '__main__':
        main()
}
```

## Función `main()`

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

## Clase `Captura_codigos`

1. Lo principal es definir los atributos de la instancia clase que en este caso serán un diccionario con los datos de las coordenadas y una cadena de caracteres para imprimir en el archivo llamados `dato_coordenada` y `cadena` respectivamente; estos se inicializan como un diccionario vacío y una cadena también vacía.
    
```python
{
    class Captura_codigos:

        #Se define el constructor o clase fundamental con los atributos que tendrán las instancias de la clase.
        def __init__(self):
            self.dato_coordenada={}
            self.cadena=""
}
```

2. La función `read_barcodes(self, frame)` presentada a continuación:

a. ### Función `read_barcodes(self, frame)`

i. Esta contiene la variable que almacena todos los códigos de barras de la lectura que se nombra como `barcodes`, se hace uso de la librería `pyzbar` para hacer la decodificación correspondiente y se usan como parámetros el marco obtenido de la lectura en tiempo real (`frame`) y el atributo `symbols=[ZBarSymbol.CODE128]` que permite la lectura de solamente el tipo de códigos de barras que se están usando, lo cual mejora el reconocimiento y desempeño del programa. **En caso de leer otro tipo de códigos de barras se tendrá que cambiar el atributo symbols por la propiedad correspondiente.**

```python
{
    #Función que se encarga de leer los códigos de barras, recibe el marco o la captura de la pantalla actual
    def read_barcodes(self, frame):
        #Variable que almacena 
        barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])
}
```

ii. Siguiente a ello, siempre que se entra a la función se limpia el diccionario `dato_coordenada` para no tener problemas con los datos almacenados antes. Siguiente a ello se encuentra un ciclo que permitirá extraer las coordenadas que conforman el triángulo del código de barras definidas como el inicio de la coordenada en y (`y`), el inicio de la coordenada en x (`x`), el alto del rectángulo (`h`) y el ancho del rectángulo (`w`), para cada uno de los códigos esas coordenadas estarán guardadas en el atributo `rect` de cada elemento en el arreglo `barcodes` extrayendose gracias a la instrucción `barcode.rect`.

```python
{
        #Se limpia el diccionario de los datos de las coordenadas.
        self.dato_coordenada={}
        #Ciclo para recorrer todos los códigos de barras encontrados.
        for barcode in barcodes:
            #Se extraen las coordenadas del rectángulo decodificado en cada código para su futuro procesamiento.
            x, y, w, h = barcode.rect      
}
```

iii. Continuando el proceso, se hace uso de la instrucción `barcode.data.decode('utf-8')` con el fin de asignar el valor leído del código de barras a la variable `barcode_text`. Después se hace uso de la librería `cv2` con el atributo `rectangle` para enviar los parámetros del rectángulo dibujado en pantalla al reconocer los códigos de barras, los parámetros de la instrucción `cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)` se componene respectivamente del marco en cuestión, el punto de inicio del rectángulo, el punto final del rectángulo, el color (dado como un grupo de datos RGB) y el grosor de la línea en pixeles, **todos los parámetros son modificables dependiendo de las necesidades.** 

```python
{
            barcode_text = barcode.data.decode('utf-8')      
            #Se definen las coordenadas, el color y el grosor (en pixeles) de la línea del rectángulo que se muestra 
            #en pantalla.
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)   
            #Se agregan los datos al diccionario considerando la llave como el código leído y las coordenadas x y y
            #como los datos asociados.
            self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)
}
```

iv. En este punto, se almacena cada uno de los datos en el diccionario `dato_coordenada` donde se considera que la clave es el valor de lo almacenado en `barcode_text` y los datos asociados son el punto central del rectángulo construido con las coordenadas `x, y, w, h` obtenidas antes. También, se crea un condicional que verifica si el diccionario `dato_coordenada` no está vacío y si además la longitud de datos que contiene es igual al número de bloque esperado, dado por `NUM_BLOQUES`, esto con el fin de que al realizar el cambio de los bloques no se generen datos intermedios innecesarios, si las condiciones anteriores se cumplen, se envían los datos en `dato_coordenada` para su ordenamiento. Finalmente, se retorna el marco actual definido como `frame`.

```python
{
            #Se agregan los datos al diccionario considerando la llave como el código leído y las coordenadas x y y
            #como los datos asociados.
            self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)

        #Condicional para verificar que el arreglo contenga datos y a su vez estos datos sean igual al número de bloques
        #esperado, si esto se cumple, se envía el diccionario a la función de ordenamiento.
        if(len(self.dato_coordenada)>0 and len(self.dato_coordenada)==NUM_BLOQUES):
            self.ordena(self.dato_coordenada)

        #Se hace un retorno del marco actual.
}
```
