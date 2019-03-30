import numpy as np
import cv2
from time import sleep
import serial
import math
import datetime
import sys
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

plist = []

Kp = 0.3
Ki = 0.2
Kd = 0.1
#During the execution we changed the values of the Kp, Ki and Kd values and ran for the 
#set of the requested things i.e Kp=0.2 and,3 
#Kp=0.2 and Ki=0.2 
#Optimal values for Kp Ki and Kd ---- 0.6 0.2 and 0.01 


def PID(required_angle, current_angle):
    global integral, error_previous
    error = required_angle - current_angle
    integral = integral + Ki * error
    out = Kp*error + integral + Kd*(error - error_previous)
    error_previous = error
    return out




#get the co-ordinates for the green center
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    greentuple = ([17, 100, 15], [50, 200, 56])
    lower = np.array([17, 100, 15], dtype = "uint8")
    upper = np.array([50, 200, 56], dtype = "uint8")
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Input", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(10)
    if chr(key & 255) == 'p':
        print("Green")
        #compute the area of the green circle
        im_gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        rows, cols = im_bw.shape
        up = 9999
        left = 9999
        right = 0 
        down = 0
        for i in range(rows):
            for j in range(cols):
                if(im_bw[i, j] > 0):
                    if(i>down):
                        down = i
                    if(i<up):
                        up = i
                    if(j<left):
                        left = j
                    if(j>right):
                        right = j
                        
        amidi = int((down+1-up)/2) + up
        amidj = int((right+1-left)/2) + left   
        g=amidj
        #plist.append(tuple((midi, midj)))        
        break

#get the three red co-ordinates        
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #print(ret)
    #print(frame)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #frame = cv2.imread("img.jpg")
    redtuple = ([17, 15, 100], [50, 56, 200])
    lower = np.array([17, 15, 100], dtype = "uint8")
    upper = np.array([50, 56, 200], dtype = "uint8")
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Input", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(10)
    if chr(key & 255) == 'p':
        print("Red")
        im_gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        rows, cols = im_bw.shape
        up = 9999
        left = 9999
        right = 0 
        down = 0
        for i in range(rows):
            for j in range(cols):
                if(im_bw[i, j] > 0):
                    if(i>down):
                        down = i
                    if(i<up):
                        up = i
                    if(j<left):
                        left = j
                    if(j>right):
                        right = j
                        
        bmidi = int((down+1-up)/2) + up
        bmidj = int((right+1-left)/2) + left
        r=bmidj
        #plist.append(tuple((midi, midj)))
        break
        
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    redtuple = ([17, 15, 100], [50, 56, 200])
    lower = np.array([17, 15, 100], dtype = "uint8")
    upper = np.array([50, 56, 200], dtype = "uint8")
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Input", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(10)
    if chr(key & 255) == 'p':
        print("Red2")
        im_gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        rows, cols = im_bw.shape
        up = 9999
        left = 9999
        right = 0 
        down = 0
        for i in range(rows):
            for j in range(cols):
                if(im_bw[i, j] > 0):
                    if(i>down):
                        down = i
                    if(i<up):
                        up = i
                    if(j<left):
                        left = j
                    if(j>right):
                        right = j
                        
        cmidi = int((down+1-up)/2) + up
        cmidj = int((right+1-left)/2) + left
        #plist.append(tuple((midi, midj)))
        break

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    redtuple = ([17, 15, 100], [50, 56, 200])
    lower = np.array([17, 15, 100], dtype = "uint8")
    upper = np.array([50, 56, 200], dtype = "uint8")
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Input", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(10)
    if chr(key & 255) == 'p':
        print("Red3")
        im_gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        rows, cols = im_bw.shape
        up = 9999
        left = 9999
        right = 0 
        down = 0
        for i in range(rows):
            for j in range(cols):
                if(im_bw[i, j] > 0):
                    if(i>down):
                        down = i
                    if(i<up):
                        up = i
                    if(j<left):
                        left = j
                    if(j>right):
                        right = j
                        
        dmidi = int((down+1-up)/2) + up
        dmidj = int((right+1-left)/2) + left
        
        #plist.append(tuple((midi, midj)))
        break

#we have the 4 points
print(plist)

start = 0
length = 0
angle=999
r=abs(g-r)
print(r)

angleb = 0
lista = []
listb = []
timearr=[]
timearrb=[]
listb.append(0)
err_term = 0

array_a = np.float32([[0,0],[100,0],[70,70],[0,100]])
array_b = np.float32([[amidj,amidi],[bmidj,bmidi],[cmidj,cmidi],[dmidj,dmidi]])
M = cv2.getPerspectiveTransform(array_b, array_a)
print(M)
print(array_a)
print(array_b)
#sys.exit()


ser = serial.Serial('COM5', 9600) # Establish the connection on a specific port
sleep(20)
ser.close()

old_angle = 0

a1 = []
a2 = []

#start sending data based on the keystroke
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    redtuple = ([17, 15, 100], [50, 56, 200])
    lower = np.array([17, 15, 100], dtype = "uint8")
    upper = np.array([50, 56, 200], dtype = "uint8")
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("Input", frame)
    cv2.imshow("Output", output)
    key = cv2.waitKey(10)
    
    if chr(key & 255) == 'p':
        break;
    print("Calculate")
    im_gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    rows, cols = im_bw.shape
    up = 9999
    left = 9999
    right = 0 
    down = 0
    for i in range(rows):
        for j in range(cols):
            if(im_bw[i, j] > 0):
                if(i>down):
                    down = i
                if(i<up):
                    up = i
                if(j<left):
                    left = j
                if(j>right):
                    right = j
    
    
    #oldi = midi
    #oldj = midj
    #oldangle = angle
    
    midi = int((down+1-up)/2) + up
    midj = int((right+1-left)/2) + left
    
    diffj = abs(g-midj)
    
    print(diffj)
    if(diffj>r):
        diffj = r
    angle = math.degrees(math.acos(diffj/r))
    if g>midj:
        angle = 180-angle
    print(angle)
    
    lista.append(int(math.degrees(angle)))
    
    #err_term
    
    a1.append(angle)
    a2.append(old_angle)
    ser.open()
    
    #ser.write(str(chr(int(angle))).encode('ascii', 'ignore')) # Convert the decimal number to ASCII then send it to the Arduino
    timearr.append(str(datetime.datetime.time(datetime.datetime.now())))
    ser.write(bytes([int(old_angle)]))
    ser.write(bytes([int(angle)]))
    #err_angle = angle-old_angle
    err_angle = PID(angle, old_angle)
    if(err_angle > 0):
        if(err_angle>10):
            vel = 10
        else:
            vel = err_angle
    else:
        if(err_angle<-10):
            vel = -10
        else:
            vel = err_angle
    ser.write(bytes([int(vel+100)]))
    print(ser.readline()) # Read the newest output from the Arduino
    timearrb.append(str(datetime.datetime.time(datetime.datetime.now())))
    listb.append(int(math.degrees(angle)))
    angleb = int(math.degrees(angle))
    sleep(0.1) # Delay for one tenth of a seczzzond
    #old_angle = angle
    print(ser.readline())
    old_angle+=vel
    #break
    sleep(0.1)
    ser.close()
    
plt.plot(a1,'ro')
plt.plot(a2,'g')
plt.show()
cap.release()