import cv2
img = cv2.imread(r"C:\Users\Lenovo\Desktop\computer_vision\hands.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh_val, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"Otsu's : {thresh_val}")
_,th_binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("original",img)
cv2.imshow("Otsu's_binary",binary)
cv2.imshow("THRESH_binary",th_binary)
cv2.waitKey(0)
cv2.destroyAllWindOWS()

