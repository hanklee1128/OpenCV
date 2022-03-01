import cv2

#儲存檔案 cv2.imwrite("要存的檔名",圖片變數,儲存類型參數)

img=cv2.imread("bear.jpg")
blurimg=cv2.GaussianBlur(img,(15,15),10)

cv2.imwrite("bluringPict.jpg",blurimg)