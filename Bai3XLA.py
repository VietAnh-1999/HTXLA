import cv2
img = cv2.VideoCapture(0)

while True:
    _,image = img.read()
    cv2.imshow("",image)
    if cv2.waitKey(1) == ord('q'):
        break