import cv2
import numpy as np

#4.2類型轉換函數
"""
在openCV內,可以使用cv2.cvtColor()來實現色彩空間的轉換
語法如下:
  dst=cv2.cvtColor(src,code,[dstCn])
  
  scr:表示原始輸入影像,可以是uint-8 or uint-16 
  dst:表示輸出影像,與原始具有相同的data type與深度
  code:表示色彩空間轉換碼
  dstCn:是靶心圖表面的channel數,default為0;default為channel數自動透過原始輸入影像和code獲得
"""
#example
img=np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("img=\n",img)
print("rst=\n",rst)
