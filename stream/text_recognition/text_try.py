import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
import pyttsx3
speaker = pyttsx3.init()
speaker.setProperty("rate", 150)
speaker.setProperty("voice", 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')



pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Owner\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('a.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
all_y_coord=[]
all_leters_dict={}
counter=1
letter='letter'
x='x'
y='y'
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    #print(b[0])
    all_y_coord.append(b[2])
    all_leters_dict[counter]={letter:b[0],x:b[1],y:b[2]}
    #x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    # cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    # cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    counter+=1


#cv2.imshow('img', img)
cv2.waitKey(0)


#count the most y
y_dict={}
all_y_coord=[int(x) for x in all_y_coord]
for each in all_y_coord:
    if each not in y_dict:
        y_dict[each]=0
    y_dict[each]+=1

first_most_y_coordiantes=[ x for x,y in y_dict.items() if y>1 ]
#(first_most_y_coordiantes)




#print("".join(all_leters))
#print(all_leters_dict)

# find the words in horisontal directions
words={}
range_letter=3
for each_y in first_most_y_coordiantes:
    words[each_y] = []
    for _,value in all_leters_dict.items():
        if each_y-range_letter<=int(value[y])<=each_y+range_letter:
            words[each_y].append(value[letter])

sentense=[''.join(word) for _,word in words.items()]

text=f"{len(sentense)} found sentenses. They are: {', '.join(sentense)}"
speaker.say(text)
speaker.runAndWait()


