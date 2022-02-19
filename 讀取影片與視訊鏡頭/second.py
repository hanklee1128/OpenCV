import cv2

#VideoCapture("要抓取的mp4檔名")
cap=cv2.VideoCapture("thumb.mp4")

while True:
    ret,frame=cap.read()
    
    
    if ret:
        #resize frame
        frame=cv2.resize(frame,(0,0),fx=0.3,fy=0.3)
        
        cv2.imshow("video",frame)
    else:
        break

    #waitKey(delay時間)會讀取鍵盤上的按鍵,若按q則break while loop
    if cv2.waitKey(10)==ord("q"):
        break
    