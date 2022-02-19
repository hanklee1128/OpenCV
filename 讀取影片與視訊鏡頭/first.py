import cv2

#VideoCapture("要抓取的mp4檔名")
cap=cv2.VideoCapture("thumb.mp4")

#影片變數.read()函式回傳兩個值
#首先回傳第一個值為讀取下一幀有沒有成功=>為一布林值
#接著回傳第二個值為讀取到下一幀的圖片
#ret, frame =cap.read()
"""
讀取一幀,若要連續成影片則可用迴圈表示每一幀
if ret:
    cv2.imshow("video",frame)

cv2.waitKey(0)
"""

while True:
    ret,frame=cap.read()

    if ret:
        cv2.imshow("video",frame)
    else:
        break
    cv2.waitKey(1)#delay 1ms