
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Owner\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'



img = cv2.imread("d.jpg")
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
#img = cv2.imread("a.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Convert the image to gray scale
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)# Performing OTSU threshold
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10)) #10,10
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
im2 = img.copy()

found_wors=[]
# hImg, wImg,_ = img.shape
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    # text = pytesseract.image_to_string(cropped)
    # print(text)
    # found_wors.append(text)
cv2.imshow('img', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(found_wors)
# text=f"{len(found_wors)} found sentenses. They are: {', '.join(found_wors)}"


