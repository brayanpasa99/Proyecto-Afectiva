import cv2
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

class Captura_codigos:
    
    def __init__(self):
        self.dato_coordenada={}

    def read_barcodes(self, frame):
        barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])
        while(len(self.dato_coordenada)<3):
            for barcode in barcodes:
                x, y, w, h = barcode.rect      
                barcode_text = barcode.data.decode('utf-8')      
                cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)   
                if(self.dato_coordenada.has_key(barcode_text)):
                    self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)
                elif(not self.dato_coordenada.has_key(barcode_text)):
                    self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)
                else:
                    print("ERROR de ejecucion")
            return frame
        return frame

    def ordena(self):
        print("Ordena")

    #def guarda_coordenadas(self, barcode_text, coordenadas)

def main():
    Capturar = Captura_codigos()
    camera = cv2.VideoCapture(2)
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