import cv2
import numpy as np
import random

#讀取彩色影像,並對像素進行存取與修改
img=cv2.imread("lenna.jpg")
cv2.imshow("before",img)

print("存取img[0,0]=",img[0,0])
print("存取img[0,0,0]=",img[0,0,0])
print("存取img[0,0,1]=",img[0,0,1])
print("存取img[0,0,2]=",img[0,0,2])
print("存取img[50,0]=",img[50,0])
print("存取img[100,0]=",img[100,0])
#region1
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img[i,j,k]=255 #img[0:50,0:100]存成白色
#region2
for i in range(50,100):
    for j in range(0,100):
        img[i,j]=[128,128,128] #灰色
#region3
for i in range(100,150):
    for j in range(0,100):
        img[i,j]=0 #黑色

cv2.imshow("after",img)
print("修改後img[0,0]=",img[0,0])
print("修改後img[0,0,0]=",img[0,0,0])
print("修改後img[0,0,1]=",img[0,0,1])
print("修改後img[0,0,2]=",img[0,0,2])
print("修改後img[50,0]=",img[50,0])
print("修改後img[100,0]=",img[100,0])
cv2.waitKey(0)
cv2.destroyAllWindows()

#使用numpy.array存取像素
"""
numpy提供item(),itemset()來存取和修改像素值,且這兩個函式都經過最佳化處理,能
夠更高效地加強處理效率

item()能夠更高效地存取影像的像素點,語法如下:
item(行,列)

itemset()可以用來修改像素值,語法如下:
itemset(索引值,新值)
"""

#用一亂數組來模擬灰階影像,並進行簡單處理
#img=np.random.randint(low,high,size,dtype=)
img=np.random.randint(10,99,size=[5,5],dtype=np.uint8)
print("img=\n",img)
print("讀取像素點img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255) #寫入新值為255
print("修改後img=\n",img)
print("修改後像素點img.item(3,2)=",img.item(3,2))

#產生灰階影像,讓其中像素值均為亂數
img=np.random.randint(0,256,size=[256,256],dtype=np.uint8)
cv2.imshow("demo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=cv2.imread("lenna.jpg",0)#存成灰階影像
cv2.imshow("before",img)
print("讀取像素點img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改後的像素點img.item(3,2)=",img.item(3,2))
#測試修改一個區域的像素值
for i in range(10,100):
    for j in range(80,100):
        img.itemset((i,j),255)
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()

#彩色影像
"""
item(行,列,通道)
itemset(三元組索引值,新值)
"""
img=np.random.randint(10,99,size=[2,4,3],dtype=np.uint8)
print("img=\n",img)
print("讀取像素點img[1,2,0]=",img.item(1,2,0))
print("讀取像素點img[0,2,1]=",img.item(0,2,1))
print("讀取像素點img[1,0,2]=",img.item(1,0,2))
img.itemset((1,2,0),255) #寫入新值為255
img.itemset((0,2,1),255)
img.itemset((1,0,2),255)
print("修改後img=\n",img)
print("修改後像素點img[1,2,0]=",img.item(1,2,0))
print("修改後像素點img[0,2,1]=",img.item(0,2,1))
print("修改後像素點img[1,0,2]=",img.item(1,0,2))

#產生彩色影像,讓其中像素值均為亂數
img=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
cv2.imshow("demo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#讀取彩色影像,進行存取與修改
img=cv2.imread("lenna.jpg")
cv2.imshow("before",img)
print("讀取像素點img.item(0,0,0)=",img.item(0,0,0))
print("讀取像素點img.item(0,0,1)=",img.item(0,0,1))
print("讀取像素點img.item(0,0,2)=",img.item(0,0,2))
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img.itemset((i,j,k),255)
print("修改後素點img.item(0,0,0)=",img.item(0,0,0))
print("修改後像素點img.item(0,0,1)=",img.item(0,0,1))
print("修改後素點img.item(0,0,2)=",img.item(0,0,2))
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()

#有興趣區域Region of Interest(ROI)
img=cv2.imread("lenna.jpg")
face=img[100:240,130:250]
cv2.imshow("origin",img)
cv2.imshow("face",face)
#對face打碼
blurface=cv2.GaussianBlur(face,(15,15),10)
img[100:240,130:250]=blurface
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()
