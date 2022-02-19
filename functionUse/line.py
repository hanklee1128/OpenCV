import cv2
from cv2 import FILLED
import numpy as np


img=np.zeros((600,600,3),np.uint8)

#畫線 cv2.line()
#參數:img圖片,起始座標(0,0),終點座標(400,300),線的顏色由(B,G,R)控制
#最後1為線的寬度
cv2.line(img,(0,0),(400,300),(255,0,0),1)

#畫矩形
cv2.rectangle(img,(0,0),(400,300),(100,20,150),1)

#填滿矩形
cv2.rectangle(img,(500,500),(600,600),(100,20,150),cv2.FILLED)

#畫圓
#圓心(45,45),半徑15,顏色(255,255,255),線寬1
cv2.circle(img,(45,45),15,(255,255,255),1)

#填滿圓
cv2.circle(img,(45,45),10,(0,255,255),cv2.FILLED)

#寫文字
#文字左下角的座標(100,500),字體cv2.FONT...,1為字的大小,(255,255,255)BGR顏色,2為文字粗度
cv2.putText(img,"hello world",(100,500),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)



cv2.imshow("black",img)
cv2.waitKey(0)
