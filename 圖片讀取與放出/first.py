import cv2

img=cv2.imread("dog.jpg")#imread("讀取圖片的名稱")

cv2.imshow("img",img)#imshow("開啟圖片的檔名",要讀的變數)
cv2.waitKey(0)#等待按一個鍵後關閉圖檔