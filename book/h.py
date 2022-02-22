import cv2
import numpy as np

#影像加密和解密
"""
可以透bitwise_xor實現加密和解密
透過對原始影像與金鑰對象進行bitwise_xor,可以加密
透過對加密後的影像與金鑰影像進行bitwise_xor,可以解密

"""

lenna=cv2.imread("lenna.jpg",0)#原始影像
row,col=lenna.shape
key=np.random.randint(0,256,size=[row,col],dtype=np.uint8)#金鑰
secretimg=cv2.bitwise_xor(lenna,key)#加密後的影像
knowimg=cv2.bitwise_xor(secretimg,key)#解密後的影像

cv2.imshow("orign",lenna)
cv2.imshow("encode",secretimg)
cv2.imshow("decode",knowimg)
cv2.imshow("key",key)
cv2.waitKey()
cv2.destroyAllWindows()


#數字浮水印
"""
將一個需要隱藏的二值影像資訊嵌入載體影像的二值影像,進一步實現將二值影像隱藏的目的.
由於二值影像處於載體影像的最低有效位(Least Significant Bit,LSB)上,所以對於載體影像的影像非常不明顯
example:
載體影像為:lenna的圖片
想要隱藏在載體影像上的二值影像為一文字:(版權所屬,請勿盜用)

原理:
從位元平面的角度考慮,數字浮水印的處理過程分為下面兩步驟:
 -嵌入過程:將載體影像的第0個位元平面取代為數字浮水印資訊的載體
 -分析過程:將載體影像的最低有效位所組成的第0個位元平面分析出來,獲得數字浮水印的資料
"""
#讀取原始載體影像
lenna=cv2.imread("lenna.jpg",0)
#讀取浮水印影像
watermark=cv2.imread("watermark.png",0)

#將浮水印影像內的值255處理為1,方便之後嵌入載體的最低位元面
w=watermark[:,:]>=255
watermark[w]=1

row,col=lenna.shape

#======嵌入過程======
#產生元素值都是254的陣列,shape與載體影像相同
t254=np.ones((row,col),dtype=np.uint8)*254
#取得leena影像的高7位元
lennaH7=cv2.bitwise_and(lenna,t254)
#將watermark嵌入lennaH7內
e=cv2.bitwise_or(lennaH7,watermark)

#=====分析過程======
#產生元素值都是1的陣列,shape與載體影像相同
t1=np.ones((row,col),dtype=np.uint8)
#從載體影像內分析浮水印影像
wm=cv2.bitwise_and(e,t1) #分析出最低位元面,即浮水印的位元面
print("wm=\n",wm)
w=wm[:,:]>0
wm[w]=255
#顯示影像
cv2.imshow("lenna",lenna)
cv2.imshow("watermark",watermark)
cv2.imshow("wm",wm)
cv2.imshow("e",e)#有浮水印的lenna圖
cv2.waitKey()
cv2.destroyAllWindows

