#切割圖片

import cv2
import  numpy as np
import random 

img=cv2.imread("dog.jpg")

new1=img[:100,:100] #切割 高0到100 寬:0到100
new2=img[:100,100:200]#切割 高0到100 寬:100到200

cv2.imshow("new1",new1)
cv2.imshow("new2",new2)
cv2.waitKey(0)