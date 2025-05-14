import cv2
print(cv2.__version__)
path = r"D:\5.HT\HTVAXLA\picture\picture1.png"  # duong dan
img = cv2.imread(path)
#img = cv2.imread('picture1.jpg')                #doc anh
cv2.imshow("",img)                               #hiem thi anh
cv2.waitKey(0)                                   #thoi gian hien thi
(h, w, d) = img.shape
print(f"rong = {w}|cao = {h}|sau = {d}")      #doc kich thuoc anh
r = 600/w
dim = (600,int(h*r))
resized = cv2.resize(img,dim)
cv2.imshow("",resized)
cv2.waitKey(0)
(R, G, B) = img[60, 60]
print(f"{R},{G},{B}")

cut_picture = img[0:300, 60:300]
cv2.imshow("",cut_picture)
cv2.waitKey(0)
# xoay anh
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45 ,1.0)
rotated = cv2.warpAffine(img, M,(w,h))
cv2.imshow("",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# luu anh
cv2.imwrite(path,rotated)