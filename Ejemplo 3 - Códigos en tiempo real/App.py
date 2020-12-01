import cv2
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.CODE128])
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        print(x, y)
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)
        #print(barcode_text, x, y, "")
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame

def main():
    camera = cv2.VideoCapture(2)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()