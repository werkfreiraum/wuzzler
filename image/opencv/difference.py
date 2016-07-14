#!/bin/env python3
import numpy as np
import cv2
import argparse
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

if not args.get("video", False):
    cap = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
    cap = cv2.VideoCapture(args["video"])

imgA = []

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    imgA.insert(0, img)
 
    # Our operations on the frame come here
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow('img', imgA[0])
    #cv2.imshow('imaHsv', img)
    if len(imgA) > 1:
        diff = cv2.absdiff(imgA[0], imgA[1])
        cv2.imshow('diff', diff)

    if len(imgA) > 5:
        diff = cv2.absdiff(imgA[0], imgA[5])
        cv2.imshow('diff5', diff)
    # Display the resulting frame
    #cv2.imshow('frame', gray)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if len(imgA) > 5:
    	imgA.pop()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
