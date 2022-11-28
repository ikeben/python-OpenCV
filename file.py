import numpy as np
import cv2
url="http://192.168.159.107:8080/video"
capture=cv2.VideoCapture(url)
#define video codec
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))#contains the output filename, fps as 20 and frame size
while True:
    ret, frame= capture.read()
    if not ret:
        print(f"cant recieve frame, Exiting.....")
        break
    out.write(frame)
    cv2.imshow("live_vide0", frame)
    if cv2.waitKey(1)==ord('q'):
        break
#release
capture.release()
out.release()
cv2.destroyAllWindows