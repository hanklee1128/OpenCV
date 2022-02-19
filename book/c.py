import cv2
import numpy as np

#影像處理

#影像的基本表示方法
"""
二值影像: 
僅黑色與白色兩種顏色的影像
在電腦中,常用矩陣來表示和處理影像
黑色為0 ;白色為1

灰階影像:
通常用256個灰階級來表示灰階影像,採用區間[0,255]來表示
純黑為0; 純白為255

彩色影像:
RGB色彩空間:三個色彩channel,個別有0~255的數值
在openCV中RGB影像空間的channel排列順序為B->G->R
"""
#用np.zeros()模擬黑色影像,並進行存取與修改
img=np.zeros((25,25),np.uint8)
print("img=\n",img)
cv2.imshow("one",img)

print("讀取像素點img[0,10]=",img[0,10])
img[0,10]=255

print("修改過的img=\n",img)
print("修改過的像素點img[0,10]=",img[0,10])
cv2.imshow("two",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#讀取灰階影像,並進行存取與修改
img=cv2.imread("lenna.jpg",0) #參數0表示存取成灰階影像
cv2.imshow("before",img)

for i in range(10,100):
    for j in range(80,100):
        img[i,j]=255
cv2.imshow("after",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#產生3Darray,用來觀察彩色影像的三個channel值的變化情況
#----藍色通道----
blue=np.zeros((300,300,3),np.uint8)
blue[:,:,0]=255
print("blue=\n",blue)
cv2.imshow("blue",blue)
#----綠色通道----
green=np.zeros((300,300,3),np.uint8)
green[:,:,1]=255
print("green=\n",green)
cv2.imshow("green",green)
 #----紅色通道----
red=np.zeros((300,300,3),np.uint8)
red[:,:,2]=255
print("red=\n",red)
cv2.imshow("red",red)

cv2.waitKey(0)
cv2.destroyAllWindows()

#產生3Darray,用來觀察彩色影像的三個channel值的變化情況
img=np.zeros((300,300,3),np.uint8)
img[:,0:100,0]=255 
img[:,100:200,1]=255
img[:,200:300,2]=255
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()