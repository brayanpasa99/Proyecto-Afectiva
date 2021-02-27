import cv2
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

class Captura_codigos:
    
    def __init__(self):
        self.dato_coordenada={}
        self.initial_positions={}
        self.current_positions={}

    def read_barcodes(self, frame):
        barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])
        while(len(self.dato_coordenada)<3):
            for barcode in barcodes:
                x, y, w, h = barcode.rect      
                barcode_text = barcode.data.decode('utf-8')      
                cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)   
                if(self.dato_coordenada.has_key(barcode_text)):
                    self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)
                    self.initial_positions = self.dato_coordenada
                    self.ordena(self.dato_coordenada)
                elif(not self.dato_coordenada.has_key(barcode_text)):
                    self.dato_coordenada[barcode_text]=x+(w/2), y+(h/2)
                    self.initial_positions = self.dato_coordenada
                    self.ordena(self.dato_coordenada)
                else:
                    print("ERROR de ejecucion")
            return frame
        return frame

    def ordena(self, coor): 
        coor_x = {}
        for key in coor:
            coor_x[key]=coor[key][0]

        valores = coor_x.values()
        llaves = coor_x.keys()

        ordenados = self.selectionSort(valores, llaves)
        self.current_positions = dict(zip(ordenados[1], ordenados[0]))
        
        print("Current", self.current_positions)
        print(ordenados[1])
        print(ordenados[0])
        print("Initial", self.initial_positions)
        self.writeFile(ordenados[1])

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

    def writeFile(self, values):
        #archivo-salida.py
        # archivo-apendice.py

        cadena = ""

        for i in range(len(values)):
            cadena = cadena +" "+ values[i]

        f = open('data.txt','a')
        f.write('\n' + cadena)
        f.close()

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