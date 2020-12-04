# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:51:00 2020

@author: Rabia Tüylek
"""

import cv2

#%% video running
video = cv2.VideoCapture("./images/video.mp4")

while(True):
    ret, frame = video.read()
    if ret == False:
        print("video is over")
        break
    
    frame = cv2.resize(frame,(1280,720))
    cv2.imshow("video ",frame)
# q tuşuna bastığında video duracak.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()


#%% Canlı video aktarımı
live_camera = cv2.VideoCapture(0)
while(True):
    ret, frame = live_camera.read()
    cv2.imshow("video",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
live_camera.release()
cv2.destroyAllWindows()




#%% Colour Operations

cam = cv2.VideoCapture("./images/graffiti.mp4")
frame_counter = 0
while(True):
    ret,frame = cam.read()
    
# frame kısmını normal video'ya aktarıyoruz ve video içinde tüm işlemleri orjinali bozulmadan yapabiliyoruz.
    
    frame_counter +=1
    if frame_counter == cam.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cam.set(cv2.CAP_PROP_POS_FRAMES,0)
        
    if ret == False :
        print("video is overr")
        break
    
    frame =cv2.resize(frame,(640,480))
    
    graffiti_gray =  cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    graffiti_hsv =  cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    graffiti_hls =  cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
    graffiti_bgra =  cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    graffiti_cıe =  cv2.cvtColor(frame,cv2.COLOR_BGR2XYZ)
    
    cv2.imshow("original", frame)
    cv2.imshow("Gray",graffiti_gray)
    cv2.imshow("hsv",graffiti_hsv)
    cv2.imshow("hls",graffiti_hls)
    cv2.imshow("bgra",graffiti_bgra)
    cv2.imshow("CIE",graffiti_cıe)
    
    if cv2.waitKey(1) & 0xFF == ("q"):
        break
    
cam.release()
cv2.destroyAllWindows()



    

    
    
    
        
    



















