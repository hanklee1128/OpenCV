import cv2
import numpy as np

img=cv2.imread("lenna.jpg")
#透過cv2.split()能夠拆分影像的channel
b,g,r=cv2.split(img)
"""
上述語法同意於下者
b=cv2.split(img)[0]
g=cv2.split(img)[1]
r=cv2.split(img)[2]
"""

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.waitKey()
cv2.destroyAllWindows()


#channel合併
#cv2.merge()可以實現影像通道的合併
bgrimg=cv2.merge([b,g,r]) #順序為Blue->Green->Red
rgbimg=cv2.merge([r,g,b])#順序為Blue->Green->Red;但是套用r,g,b的 channel值
cv2.imshow("colorful1",bgrimg)
cv2.imshow("colorful2",rgbimg)
cv2.waitKey()
cv2.destroyAllWindows()

#取得影像屬性
"""
影像處理中常用的屬性:
shape:
若為彩色影像,則回傳行數 列數與通道數的陣列
若為二值影像或灰階影像,則回傳行數 列數的陣列

size:
傳回影像的像素數目,其值為 行*列*通道數
灰階與二值影像通道數為1

dtype:
傳回影像的資料型態
"""
#屬性觀察
gray=cv2.imread("lenna.jpg",0)
color=cv2.imread("lenna.jpg")
print("gray的屬性:")
print("gray.shape=",gray.shape)
print("gray.size=",gray.size)
print("gray.dtype=",gray.dtype)
print("color的屬性:")
print("color.shape=",color.shape)
print("color.size=",color.size)
print("color.dtype=",color.dtype)


#影像運算

"""
<相加>

一.add operator " + ":
影像a(像素值為a)和影像b(像素值為b)進行add時,須遵循以下規則

 a+b   = a+b ,when a+b < or = 255
   or  = mod(a+b,256) ,when a+b > 255    
mod表示取餘數

二.cv2.add():

 a+b  = a+b ,when a+b < or =255
   or = 255 ,when a+b > 255

"""
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img1=\n",img1)
print("img2=\n",img2)
#use +
print("use +,img1+img2=\n",img1+img2)

#use cv2.add()
img3=cv2.add(img1,img2)
print("usecv2.add(),img1+img2=\n",img3)

#Compare   + and cv2.add() with picture:
a=cv2.imread("dog.jpg",0)#gray picture
b=a
result1=a+b
result2=cv2.add(a,b)
cv2.imshow("orign",a)
cv2.imshow("+ result",result1)
cv2.imshow("cv2.add() result",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
<影像加權和>
將每幅影像的加權考慮進來,可以用以下公式表示

 dst=saturate(scr1 * a+ scr2 * b + r)

saturate()表示取飽和值(最大值),做影像加權運算時,scr1與scr2的size ,dtype需要一樣

一.openCV提供函式 cv2.addWeighted(),用來實現影像的加權和(混和,融合),語法如下
 
 dst=cv2.addWeighted(scr1, alpha , scr2 , beta , gamma)

 結果影像=影像1(scr1)*alpha(係數1)+影像2(scr2)*beta(係數2)+亮度調節量(gamma)

"""
img1=np.ones((3,4),dtype=np.uint8)*100
img2=np.ones((3,4),dtype=np.uint8)*10
gamma=3
#img3=img1*0.6+img2*5+3
img3=cv2.addWeighted(img1,0.6,img2,5,gamma)
print(img3)

#from cut.py make two same shape's picture
new1=cv2.imread("new1.png",0)
new2=cv2.imread("new2.png",0)

result=cv2.addWeighted(new1,0.6,new2,0.4,0)
cv2.imshow("new1",new1)
cv2.imshow("new2",new2)
cv2.imshow("mixed",result)
cv2.waitKey()
cv2.destroyAllWindows()

#bitwise logic operation逐位元邏輯運算
"""
cv2.bitwise_and()
cv2.bitwise_or()
cv2.bitwise_xor()
cv2.bitwise_not()
"""
#dst=cv2.bitwise_and(scr1,scr2,[mask])
"""
dst表示與輸入值具有相同大小的array輸出值
scr1表示第一個array或scalar類型的輸入值
scr2表示第二個array或scalar類型的輸入值
mask表示可選操作隱藏,8bit單通道array
"""
a=np.random.randint(0,255,(5,5),dtype=np.uint8)
b=np.zeros((5,5),dtype=np.uint8)
b[0:3,0:3]=255
b[4,4]=255
c=cv2.bitwise_and(a,b)
print("a=\n",a)
print("b=\n",b)
print("c=\n",c)
