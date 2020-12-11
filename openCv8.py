# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:35:09 2020

@author: Rabia Tüylek
"""

import numpy as np
import cv2
#%% Erosion dilation
#resimdeki  pürüzlükleri düzeltme
image = cv2.imread("./images/acm_noise_2.png",0)
image = cv2.resize(image,(600,400))

kernel = np.ones((5,5),np.uint8)
close = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("new image",close)
cv2.imshow("original",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Kontorlü Renk Tespiti 
cam = cv2.VideoCapture(0)
lower_tresh = (56,107,69)
upper_tresh =(147,255,217)

kernel = np.ones((5,5),np.uint8)

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_tresh,upper_tresh)
    mask = cv2.bitwise_and(mask, mask, mask = mask)
    
    mask = cv2.erode(mask,kernel,iterations=1)
    mask = cv2.dilate(mask,kernel,iterations=1)
    
    contors = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2]
    cv2.drawContours(frame,contors, -1,(0,255,0),3)
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



