import cv2

#開啟視窗
#cv2.namedWindow("視窗名稱",視窗標籤)
#視窗標籤種類:
"""
cv2.WINDOW_AUTOSIZE 隨影像自動調整,不能改變視窗大小,為系統默認值
cv2.WINDOW_FREERATIO 可隨意改變影像及視窗大小
cv2.WINDOW_KEEPRATIO 改變影像大小時會維持原來比例,可改變視窗大小
cv2.WINDOW_FULLSCAREEN 視窗為全螢幕,不能改變視窗大小
cv2.WINDOW_NORMAL 可以改變視窗大小
cv2.WINDOW_OPENGL 支援OpenGL(開放式程式庫)
"""

#關閉視窗
#1. cv2.destroyWindow("視窗名稱") 關閉視窗

#2. cv2.destroyAllWindows() 關閉所有視窗



#存影像變數
#影像變數=cv2.imread(影像檔案路徑,讀取標籤)
"""
cv2.IMREAD_COLOR 讀取彩色影像,值為1,為系統默認值
cv2.IMREAD_GRAYSCALE  讀取灰階影像,值為0
cv2.IMREAD_UNCHANHE 讀取影像之原始模式,值為 -1
"""

#在視窗中顯示影像
# cv2.imshow("視窗名稱",影像變數)
#可用imshow()直接創一個新的視窗

#等待數秒關閉影像
# cv2.waitKey(n) 等待n毫秒 若n為0則表示等待無限久,直到按下任意鍵後才繼續執行程式
#結合 ord()函式 可以讀取按鍵上的ASCII code來達成選擇功能


#Exercise1
cv2.namedWindow("colorful")
cv2.namedWindow("gray")
img1=cv2.imread("dog.jpg")#彩色為默認
img2=cv2.imread("dog.jpg",0)#灰階值為0
cv2.imshow("colorful",img1)
cv2.imshow("gray",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Exercise2
img3=cv2.imread("dog.jpg")
img4=cv2.imread("dog.jpg",0)
#透過waitKey()回傳的值,給定不同的功用
cv2.imshow("demo",img3)
key=cv2.waitKey()
if key ==ord("a"):
    cv2.imshow("pressa",img3)
elif key ==ord("b"):
    cv2.imshow("pressb",img4)

cv2.waitKey(0)
