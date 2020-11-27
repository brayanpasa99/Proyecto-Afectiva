import cv2

camera = cv2.VideoCapture(1)
ret, frame = camera.read()

while ret:
  ret, frame = camera.read()
  cv2.imshow('Barcode reader', frame)
  if cv2.waitKey(1) & 0xFF == 27:
    break
    
camera.release()
cv2.destroyAllWindows()