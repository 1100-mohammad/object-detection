import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.5,maxHands=2)

while True:
    ret,image = cap.read()
    _,image = detector.findHands(image)
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)

    cv2.imshow("result",image)
    if cv2.waitKey(1)& 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
