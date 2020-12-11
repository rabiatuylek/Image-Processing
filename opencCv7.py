# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:26:30 2020

@author: Rabia Tüylek
"""
import numpy as np
import cv2

#%% sobel = derivative

sudoku = cv2.imread("./images/sudoku.png")
sudoku_gray= cv2.cvtColor(sudoku, cv2.COLOR_BGR2GRAY)
# türev işlemlerinde resim her zaman gri renkte olmalı ya da gri renge çevirilmeli.
cv2.imshow("sudoku", sudoku)
#cv2.imshow("gray",sudoku_gray)
# x e göre türev
sobelx = cv2.Sobel(sudoku_gray, cv2.CV_32F, 1,0, ksize=5)
# y ye göre türev 
sobely = cv2.Sobel(sudoku_gray, cv2.CV_32F, 1,0, ksize = 5)
# laplace equations 
laplace = cv2.Laplacian(sudoku_gray, cv2.CV_32F)

cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)
cv2.imshow("LAPLACE", laplace)

cv2.waitKey(0)
cv2.destroyAllWindows()


#%% Canny Edge = resmin ana hatlarını çıkarmak

images = cv2.imread("./images/ground.jpg",0)
# resim griye çevrildi.
#images = cv2.resize(images,(500,750))
canny_edge = cv2.Canny(images,600,700)

cv2.imshow("ground",images)
cv2.imshow("canny_edge",canny_edge)

cv2.waitKey(0)
cv2.destroyAllWindows()


#%% Histogram 
resim = cv2.imread("./images/very_dark.jpg")
resim = cv2.resize(resim,(600,400))

resim_gray = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
# resim daha karanlıkken histogram komutuyla daha aydınlık olavak.
hist = cv2.equalizeHist(resim_gray)
final = np.hstack((resim_gray,hist))

cv2.imshow("final_picture",final)

cv2.waitKey(0)
cv2.destroyAllWindows()






#%% Color Range
def nothing(x):
    # any operation
    pass

video = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("Lower-hue", "Trackbars", 0,180, nothing)
cv2.createTrackbar("Lower-saturation", "Trackbars", 66,255, nothing)
cv2.createTrackbar("Lower-value", "Trackbars", 134,255, nothing)
cv2.createTrackbar("Upper-hue", "Trackbars", 180,180, nothing)
cv2.createTrackbar("Upper-saturation", "Trackbars", 255,255, nothing)
cv2.createTrackbar("Upper-value", "Trackbars", 243,255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while(True):
    ret, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_h =cv2.getTrackbarPos("Lower-Hue", "Trackbars")
    lower_s =cv2.getTrackbarPos("Lower-Saturation", "Trackbars")
    lower_v =cv2.getTrackbarPos("Lower-Value", "Trackbars")
    upper_h =cv2.getTrackbarPos("Upper-hue", "Trackbars")
    upper_s =cv2.getTrackbarPos("Upper-saturation", "Trackbars")
    upper_v =cv2.getTrackbarPos("Upper-Value", "Trackbars")
    

    lower = np.array([lower_h, lower_s, lower_v])
    upper = np.array([upper_h,upper_s, upper_v])

# masking
    mask = cv2.inRange(hsv, lower,upper)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
















































































