import cv2
import numpy as np

img1=cv2.imread("chicken.png",0)
img2=cv2.imread("sun.png",0)

print("img1.shape=",img1.shape)
print("img2.shape=",img2.shape)

#cut two picture to same shape 860*859
new1=img1[255:1116,:]
new2=img2[:,:]

cv2.imwrite("new1.png",new1)
cv2.imwrite("new2.png",new2)