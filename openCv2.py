# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:45:14 2020

@author: Rabia Tüylek
"""
import cv2
import os
import matplotlib.pyplot as plt

os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = "0"
#&& resim bastırma
image = cv2.imread("./images/Logo.png")
cv2.imshow("open cv resim", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% pixel size
images2 = cv2.imread("./images/Istanbul.jpeg")
print("size:" , images2.size)
print("shape : ", images2.shape)

cv2.imshow("istanbul",images2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
images2 = cv2.imread("./images/Istanbul.jpeg")
copy_im2 = images2.copy()
new = copy_im2[175:350, 0:900]

copy_im2[350:525, 0:900] = new

cv2.imshow("istanbul", copy_im2)
cv2.imshow("new", new)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% resimlerde cerceveleme

colour = cv2.imread("./images/Logo2.png")
cv2.imshow("resim", colour)

green = [0,255,0]
red = [0,0,255]

border1 = cv2.copyMakeBorder(colour,15,15,15,15,cv2.BORDER_WRAP)
border2 = cv2.copyMakeBorder(colour,15,15,15,15,cv2.BORDER_REFLECT)
border3 = cv2.copyMakeBorder(colour,15,15,15,15,cv2.BORDER_REFLECT101)
border4 = cv2.copyMakeBorder(colour,15,15,15,15,cv2.BORDER_REPLICATE)
border5 = cv2.copyMakeBorder(colour,15,15,15,15,cv2.BORDER_CONSTANT,value = green)
border6 = cv2.copyMakeBorder(colour,15,15,15,15,cv2.BORDER_ISOLATED,value =red)

image_dict = {"wrap":border1, "reflect":border2, "reflect101":border3, 
              "replicate":border4, "constant_green":border5, "isolated_red":border6}

i = 1
for key,value in image_dict.items():
    plt.subplot(2,3,i)
    plt.imshow(value)
    plt.title(key)
    plt.axis("off")
    i =i+1
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% resim çerçeveleme 2

acm = cv2.imread("./images/acm.png")
red =[0,0,255]
border_acm = cv2.copyMakeBorder(acm,15,15,15,15,cv2.BORDER_ISOLATED, value = red)

cv2.imshow("new image", border_acm)
cv2.waitKey(0)
cv2.destroyAllWindows()










