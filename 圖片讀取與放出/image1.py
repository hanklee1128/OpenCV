import cv2
import  numpy as np
import random

img=cv2.imread("dog.jpg")
print(type(img))#imgage存成一numpy的陣列型態
print("======================")
print(img)
print("======================")
print(img.shape)#(259,220,3) 

"""
array shape=(2,3,4)
在最外層的中括號內有兩個中括號
在第二層中括號內有三個中括號
在最內層中括號內有四個元素

[
    [    [*,*,*,*],     [....],    [....]  ],
    [    [*,*,*,*],     [....],    [....]  ]
]
"""
#np.empty()給一個ndarray值全為隨機
# np.unit8表示0到2^8 -1
img1=np.empty((300,300,3),np.uint8)
img2=np.empty((300,300,3),np.uint8)

for row in range(300):
    for col in range(300):
        img1[row][col]=[0,255,0] #opecv 排序為B,G,R
        img2[row][col]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow("fig1",img1)
cv2.imshow("fig2",img2)
cv2.waitKey(0)
