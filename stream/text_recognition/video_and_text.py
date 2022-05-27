import cv2
import pytesseract
import numpy as np
import pyttsx3
from PIL import ImageGrab
import time
import re
pattern=r"(?P<num>([A-Z 0-9]{6,10}))"
speaker = pyttsx3.init()
speaker.setProperty("rate", 150)
speaker.setProperty("voice", 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

"""
a3456rv
EU RO 2013
BC BA 301
A 111111 
B 2390 F
D 1111111  
CC 2390 MB
123 Х 456

Good only from 2-3m and good light

"""


pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Owner\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to gray scale
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)  # Performing OTSU threshold
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))  # 10,10 18
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        #rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)

        print(text)
        valid_numers=re.finditer(pattern,text)
        if not valid_numers:
            continue
        for each_nummern in valid_numers:
            valid_=each_nummern.group('num')
            print(valid_)
            speaker.say(valid_)
            speaker.runAndWait()

        #cv2.imshow("Result", img)
        #cv2.waitKey(1)





    # #img = captureScreen()
    # #DETECTING CHARACTERES
    # hImg, wImg,_ = img.shape
    # boxes = pytesseract.image_to_boxes(img)
    # for b in boxes.splitlines():
    #     #print(b)
    #     b = b.split(' ')
    #     #print(b)
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    #     cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    # #cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
    # cv2.imshow("Result",img)
    # cv2.waitKey(1)



# cv2.imshow('img', img)
# cv2.waitKey(0)
