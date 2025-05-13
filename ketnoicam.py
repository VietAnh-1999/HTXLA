import cv2
cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()
    (w,h,r) = image.shape
    #resize_img = cv2.resize(image,(int(w*1.5),int(h*1.5)))
    cv2.imshow("video",image)
    if cv2.waitKey(1) == ord('q'):
        break