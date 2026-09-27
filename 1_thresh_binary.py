import cv2
img = cv2.imread(r"C:\Users\Lenovo\Desktop\computer_vision\detect_img.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("gray",gray)
cv2.imshow("original",img)
cv2.imshow("binary",binary)
cv2.waitKey(0)
cv2.destroyAllWindOWS()

