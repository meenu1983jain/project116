import cv2
img=cv2.imread("butterfly.jpg")
cv2.imshow("Display Image",img)
print(img)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGBTOGRAY)
cv2.imshow("grayscale",gray_img)
print(gray_img)
cv2.waitKey(0)