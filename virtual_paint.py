import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640) # To set width
cap.set(4, 480) # To set height
cap.set(10, 70) # To set brightness

# Enter your color values you wish to be detected in myColors array in similar format
myColors = [[0, 153, 144, 26, 247, 229], [24, 84, 105, 33, 177, 175], [83, 73, 35, 126, 255, 228]] 

# Enter your color values you wish to be drawn on the screen corresponding to myColors in myColorsValues array in similar format
myColorValues = [[51, 255, 255], [0, 255, 0], [255, 0, 0]]
myPoints = []

def findColor(img, myColor, myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColor: 
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValue[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count += 1        

    return newPoints

def getContours(img):
    x, y, w, h = 0, 0, 0, 0
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 20:            
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)        
            x, y, w, h = cv2.boundingRect(approx)

    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("Video", imgResult)

    if cv2.waitKey(1) & 0xFF ==ord("q"): 
        break