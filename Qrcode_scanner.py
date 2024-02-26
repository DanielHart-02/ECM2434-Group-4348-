import cv2  
from pyzbar.pyzbar import decode  
import time 

cam = cv2.VideoCapture(0)

cam.set(3, 640)  # Width
cam.set(4, 480)  # Height

while True:
    success, frame = cam.read()  

   
    for barcode in decode(frame):
        print(barcode.type)  
        print(barcode.data.decode('utf-8'))  
        time.sleep(6)  
    
    cv2.imshow("Qr_Code_Scanner", frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()
