import cv2
img=cv2.imread("dog.jpg")
#resize有兩種方法,第一:
#resize(圖片變數,(x像素數,y像素數))
img=cv2.resize(img,(300,300))
cv2.imshow("fig1",img)
cv2.waitKey(0) 

#第二:
#resize(圖片變數,縮放中心座標,fx=?,fy=?)
#fx,fy為x方向與y方向之縮放倍率
img=cv2.resize(img,(0,0),fx=2,fy=0.5)
cv2.imshow("fig2",img)
cv2.waitKey(0) 