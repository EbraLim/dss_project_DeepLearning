import sys
import cv2
import time
import datetime


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera open failed!")
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)
delay = round(1000/fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    now = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    cv2.imwrite(f'210506/pic_{now}.jpg', frame)
    time.sleep(4)


    if cv2.waitKey(delay) == 27:
        break


cap.release()
cv2.destroyAllWindows()