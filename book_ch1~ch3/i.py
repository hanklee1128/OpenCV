import numpy as np
import cv2

#臉部打碼及解碼

#讀取原影像
lenna=cv2.imread("lenna.jpg",0)
#讀取原影像shape
row,col=lenna.shape

#臉部遮罩mask
mask=np.zeros((row,col),dtype=np.uint8)
mask[70:250,70:300]=1
#設置一個key,用來打碼與解碼所使用的金耀
key=np.random.randint(0,256,size=[row,col],dtype=np.uint8)

#=====取得打碼臉=====
#使用金鑰對lenna加密
lennaXorKey=cv2.bitwise_xor(lenna,key)
#取得加密影像的臉部資訊encryptFace
encryptFace=cv2.bitwise_and(lennaXorKey,mask*255)
#將影像lenna內的臉部值設定為0,獲得noFace1
noFace1=cv2.bitwise_and(lenna,(1-mask)*255)
#獲得打碼的lenna影像
maskFace=encryptFace+noFace1

#====將打碼臉解碼=====
extractorign=cv2.bitwise_xor(maskFace,key)
#將解碼的臉部資訊分析出來
extractFace=cv2.bitwise_and(extractorign,mask*255)
#從臉部打碼的lenna內分析沒有臉部資訊的lenna影像,獲得noFace2
noFace2=cv2.bitwise_and(maskFace,(1-mask)*255)
#獲得解碼的lenna影像
extractlenna=extractFace+noFace2
#=====顯示影像=====
cv2.imshow("lenna",lenna)
cv2.imshow("mask",mask*255)
cv2.imshow("1-mask",(1-mask)*255)
cv2.imshow("key",key)
cv2.imshow("lennaXorKey",lennaXorKey)
cv2.imshow("encryptFace",encryptFace)
cv2.imshow("noFace1",noFace1)
cv2.imshow("maskFace",maskFace)
cv2.imshow("extractorign",extractorign)
cv2.imshow("extractFace",extractFace)
cv2.imshow("noFace2",noFace2)
cv2.imshow("extractlenna",extractlenna)
cv2.waitKey()
cv2.destroyAllWindows()