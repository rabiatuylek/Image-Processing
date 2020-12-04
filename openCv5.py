# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:21:39 2020

@author: Rabia Tüylek
"""
import cv2
import numpy as np
import os

os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = "0"

#%% Recording Video

live_camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.mp4",fourcc, 10.0,(640,480))

while(live_camera.isOpened()):
    ret,frame = live_camera.read()
    
    if ret == True:
        out.write(frame)
        
        cv2.imshow("Video is recording, please press q to stop recording",frame )
        
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
        
    else:
        break

live_camera.release()
out.release()
cv2.destroyAllWindows()



#%%  adding operations

x = np.uint8([29])
y = np.uint8([230])

print("numpy adding : ", np.add(x,y))
print("openCV adding : ", cv2.add(x,y))



#%% Image Adding

logo =cv2.imread("./images/opencv.png")
zebra_ = cv2.imread("./images/zebra.jpg")
# boyutları eşitle
zebra_ = cv2.resize(zebra_,(324,378))
#adding
new_photo = cv2.add(logo,zebra_)
#istenilen fotoğraf yoğunluğunu ekleme
weighted_image = cv2.addWeighted(logo,0.3,zebra_,0.8,0)

cv2.imshow("orjinal logo",logo)
cv2.imshow("zebra",zebra_)
cv2.imshow("sum",new_photo)
cv2.imshow("weighted",weighted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()




#%% Bitwise operation (logic)
first_img = cv2.imread("./images/input1.png")
second_img = cv2.imread("./images/input2.png")
cv2.imshow("first",first_img)
cv2.imshow("second",second_img)

and_operator = cv2.bitwise_and(first_img,second_img, mask = None)
or_operator = cv2.bitwise_or(first_img,second_img, mask = None)
xor_operator = cv2.bitwise_xor(first_img,second_img, mask = None)
not_op1 = cv2.bitwise_not(first_img, mask = None)
not_op2 = cv2.bitwise_not(second_img, mask = None)
cv2.imshow("and", and_operator)
cv2.imshow("or", or_operator)
cv2.imshow("xor", xor_operator)
cv2.imshow("not1", not_op1)
cv2.imshow("not2", not_op2)

cv2.waitKey(0)
cv2.destroyAllWindows()





#%% Bluring Operations

image = cv2.imread("./images/noisy_image.png")

kernel = np.ones((5,5), np.float32)/ 25
output = cv2.filter2D(image, -1, kernel)

cv2.imshow("original image", image)
cv2.imshow("blurred",output )
cv2.waitKey(0)
cv2.destroyAllWindows()




#%% Another Blurring
images = cv2.imread("./images/noisy_image_2.png")

blurring = cv2.blur(images,(11,11))
gaussian_blur = cv2.GaussianBlur(images,(11,11),0)
# median blurring netleştirir
median = cv2.medianBlur(images,5)

cv2.imshow("original image", images)
cv2.imshow("blurring", blurring)
cv2.imshow("gaussian blurring", gaussian_blur)
cv2.imshow("median blur image", median)

cv2.waitKey(0)
cv2.destroyAllWindows()




















        


