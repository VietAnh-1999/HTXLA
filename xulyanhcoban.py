import cv2
print(cv2.__version__)
path = r"D:\5.HT\HTVAXLA\picture\picture1"
img = cv2.imread('picture1.png')
cv2.imshow(img)
cv2.waitKey(0)