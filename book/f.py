import cv2
import numpy as np

#bitwise_and練習1
a=cv2.imread("lenna.jpg",0)
b=np.zeros(a.shape,dtype=np.uint8) #與a同shape,型態為uint8的0值array


c=a[70:250,70:300]
cv2.imshow("cut",c) #臉部裁切
cv2.waitKey()
cv2.destroyAllWindows()

b[70:250,70:300]=255 #讓b變數對應a臉部的區域的值為255

d=cv2.bitwise_and(a,b) #臉部的值才會呈現出來 其他為0

cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("d",d)
cv2.waitKey()
cv2.destroyAllWindows()

#bitwise_and練習2
a=cv2.imread("lenna.jpg")#彩色影像
b=np.zeros(a.shape,dtype=np.uint8)
b[70:250,70:300]=255
c=cv2.bitwise_and(a,b)
print("a.shape=",a.shape)
print("b.shape=",b.shape)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()

"""
bitwise_or轉成二進制逐位元做or運算
198 (base10)=1100 0110
219 (base10)=1101 1011
cv2.bitwise_or(198,219)=>1101 1111

bitwise_not
198 = 1100 0110

cv2.bitwise_not(198)=>0011 1001

cv2.bitwise_xor(198,219)=0001 1101
"""

#掩模(隱藏) --mask遮罩
"""
openCV中的很多函數都會指定一個掩模,例如
 
 回傳結果=cv2.add(參數1,參數2,mask=掩模)

當使用掩模時,操作只會在掩模值為不可為空的像素點上執行,並將其他像素點的值設置為0
"""
#example of mask 1
img1=np.ones((4,4),dtype=np.uint8)*3
img2=np.ones((4,4),dtype=np.uint8)*5
mask=np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4]=1
img3=np.ones((4,4),dtype=np.uint8)*66

print("img1=\n",img1)
print("img2=\n",img2)
print("初值img3=\n",img3)
print("mask=\n",mask)

img3=cv2.add(img1,img2,mask=mask)
print("add加遮罩後的img3=\n",img3)

#example of mask 2
a=cv2.imread("lenna.jpg")
w,h,c=a.shape #行 列 通道數
mask=np.zeros((w,h),dtype=np.uint8)
mask[70:250,70:300]=255
print("mask.shape=",mask.shape)
res=cv2.bitwise_and(a,a,mask=mask)#a跟a做and ,遮罩為mask
cv2.imshow("a",a)
cv2.imshow("mask",mask)
cv2.imshow("c",res)
cv2.waitKey()
cv2.destroyAllWindows()