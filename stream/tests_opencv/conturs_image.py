# import cv2
# import numpy as np
#
# # Let's load a simple image with 3 black squares
# img = cv2.imread('d.jpg')
# scale_percent = 20 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# image=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
#
#
# # Grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Find Canny edges
# #edged = cv2.Canny(gray, 300, 20)
# edged = cv2.threshold(gray, 300, 20,0)
# cv2.waitKey(0)
#
# # Finding Contours
# # Use a copy of the image e.g. edged.copy()
# # since findContours alters the image
# contours, hierarchy = cv2.findContours(edged,
# 	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# cv2.imshow('Canny Edges After Contouring', edged)
# cv2.waitKey(0)
#
# print("Number of Contours found = " + str(len(contours)))
#
# # Draw all contours
# # -1 signifies drawing all contours
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
#
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread("b.jpg")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_blue = np.array([110,50,50])
# upper_blue = np.array([130,255,255])
lower_red_a = np.array([3,50,50])
upper_red_a = np.array([3,255,255])
mask_red_a = cv2.inRange(imghsv, lower_red_a, upper_red_a)
lower_red_b = np.array([170,50,50])
upper_red_b = np.array([180,255,255])
mask_red_b = cv2.inRange(imghsv, lower_red_b, upper_red_b)
mask_red=mask_red_a+mask_red_b



contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
im = np.copy(img)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    M = cv2.moments(cnt)
    if M["m00"] !=0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(im, (cX, cY), 2, (255, 0, 0), 5)
        print(cX,cY)
    ww=w//2
    hh=h//2
    #print(x+ww, y+hh)
    #cv2.circle(im, ((x+ww), y+hh), 2, (255,0,0), 5)

    #rect = cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 0), 2)
cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
#cv2.imwrite("contours_blue.png", im)
output_img = img.copy()
output_img[np.where(mask_red==0)] = 0

# or your HSV image, which I *believe* is what you want
output_hsv = im.copy()
output_hsv[np.where(mask_red==0)] = 0


cv2.imshow('Contours', im)
cv2.waitKey(0)
cv2.destroyAllWindows()