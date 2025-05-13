import cv2
print(cv2.__version__)
path = r"D:\5.HT\HTVAXLA\picture\picture1.png"  # duong dan
img = cv2.imread(path)
#img = cv2.imread('picture1.jpg')                #doc anh
cv2.imshow("",img)                        #hiem thi anh
cv2.waitKey(0)                               #thoi gian hien thi

(h, w, d) = img.shape
print(f"rong = {w}|cao = {h}|sau = {d}")

