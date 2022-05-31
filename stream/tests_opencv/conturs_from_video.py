import cv2
import numpy as np
from PIL import ImageGrab

cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
def captureScreen(bbox=(300,300,1500,1000)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr
while True:
    timer = cv2.getTickCount()
    _,img = cap.read()
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    lower_red_a = np.array([0, 50, 50])
    upper_red_a = np.array([0, 255, 255])
    mask_red_a = cv2.inRange(imghsv, lower_red_a, upper_red_a)
    lower_red_b = np.array([175, 50, 50])
    upper_red_b = np.array([180, 255, 255])
    mask_red_b = cv2.inRange(imghsv, lower_red_b, upper_red_b)
    mask_red = mask_red_a + mask_red_b

    contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im = np.copy(img)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(im, (cX, cY), 2, (255, 0, 0), 5)
            print(cX, cY)
        ww = w // 2
        hh = h // 2
        # print(x+ww, y+hh)
        # cv2.circle(im, ((x+ww), y+hh), 2, (255,0,0), 5)

        # rect = cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 0), 2)
    cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
    cv2.imshow("Result", im)
    cv2.waitKey(1)
    # cv2.imwrite("contours_blue.png", im)
    # output_img = img.copy()
    # output_img[np.where(mask_red == 0)] = 0
    #
    # # or your HSV image, which I *believe* is what you want
    # output_hsv = im.copy()
    # output_hsv[np.where(mask_red == 0)] = 0
    #
    # cv2.imshow('Contours', output_hsv)
    # cv2.waitKey(0)
#cv2.destroyAllWindows()