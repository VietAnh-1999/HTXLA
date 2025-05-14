import cv2
cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()
    (w,h,r) = image.shape
    #resize_img = cv2.resize(image,(int(w*1.5),int(h*1.5)))
    cat_cas = cv2.CascadeClassifier('nguoi.xml')
    cat_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cats = cat_cas.detectMultiScale(cat_img)

    for(x,y,w,h) in cats:
        image = cv2.rectangle(image,(x,y),(x+w,y+h), (0,0,0),2)  # ve o vuong ảnh detect
        cv2.putText(image,"Nguoi",(x,y),cv2.FONT_ITALIC,0.5,(0,0,255))   # viet chu  vao khung

    cv2.imshow("video",image)
    if cv2.waitKey(1) == ord('q'):
        break