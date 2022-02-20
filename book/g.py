import numpy as np
import cv2

"""
f.py介紹加法運算和逐位元運算中,餐與運算的兩個運算元(參數)既可以是兩幅影像,
亦可以是一幅影像或一個純量數值

舉例來說,若想增加影像的整體亮度,可以將每一個像素值都加上一個特定值
 在實作時,可以給影像加一個統一像素值的影像,也可以給影像加上一個固定值
"""

img1=np.ones((4,4),dtype=np.uint8)*3
img2=np.ones((4,4),dtype=np.uint8)*5
print("img1=\n",img1)
print("img2=\n",img2)
img3=cv2.add(img1,img2)
print("img1+img2=\n",img3)
img4=cv2.add(img1,6)
print("img4=\n",img4)
img5=cv2.add(6,img2)
print("6+img2=\n",img5)

#***位元平面分解:
"""
將灰階影像中處於同一位元上的二進位像素值進行組合,獲得一幅二進位值影像
,該影像被稱為灰階影像的位元平面,這個過程被稱為位元平面分解
舉例來說,將一幅灰階影像內所有像素點上處於二進位位元內最低位元上的值進行組合,
可以組成[最低有效位]位元平面.

8bit gray picture每一個像素的值可為:
 val=a7*2^7+a6*2^6+....+a1*2^1+a0*2^0
 ai的值可能0or1,但其權重不同,a7的權重最大;a0的權重最小
 這表示a7的值對影像的影響最大;a0則最小
"""
#example
lenna=cv2.imread("lenna.jpg",0)#取得lenna的灰階影像
row,col=lenna.shape #將lenna這張圖的行與列分別傳到row與col
#做一0矩陣,大小為row*col*通道數
x=np.zeros((row,col,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i #2^i ,做影像的權重(a7,a6,a5....的權重)
print("x=\n",x)

row=np.zeros((row,col,8),dtype=np.uint8)
print("row=\n",row)
for i in range(8):
    row[:,:,i]=cv2.bitwise_and(lenna,x[:,:,i])
    mask=row[:,:,i]>0 #mask為一布林值 判斷為>0為真,反之則為假
    row[mask]=255
    cv2.imshow(str(i),row[:,:,i])
print("row=\n",row)
print("mask=\n",mask)
cv2.waitKey()
cv2.destroyAllWindows()