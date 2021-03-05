# Inicio del programa 

Este se da con la instrucción que busca la función `main()` en el archivo para poder ejecutarla.

```python
{
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
    while ret:
        ret, frame = camera.read()
        frame = Capturar.read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
}
```

4. Al finalizar la ejecución del programa se detiene la captura y se destruyen todas las ventanas.

```python
{
    camera.release()
    cv2.destroyAllWindows()
}
```
