import os
import argparse
import cv2
import numpy as np
import sys
import time
from threading import Thread
import importlib.util
import json
from pathlib import Path
import pyautogui

fr = 1
cv2.namedWindow('Selector', 1)
mp4 = cv2.VideoCapture(sys.argv[1])
is_opened = mp4.isOpened()
#print(is_opened)

config = {"boxes":[]}
cac = []
order = 0

drawing = False
ix,iy = -1,-1
mouse_params = [-1, -1, -1, -1]

(flag, frame) = mp4.read()

def onMouse(event, x, y, flags, param):
    global ix,iy,drawing, frame, mouse_params, config
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(frame,(ix,iy),(x,y),(0,250,0), 2)
        mouse_params = [ix, iy, x, y]
        config["boxes"] += [[min(mouse_params[0], mouse_params[2]), min(mouse_params[1], mouse_params[3]), max(mouse_params[0], mouse_params[2]), max(mouse_params[1], mouse_params[3]) ]]
        mouse_params = [-1, -1, -1, -1]

cv2.setMouseCallback('Selector', onMouse)

while 1:
    cv2.imshow('Selector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

fps = mp4.get(cv2.CAP_PROP_FPS) 
print(fps)
widght = mp4.get(cv2.CAP_PROP_FRAME_WIDTH)
height = mp4.get(cv2.CAP_PROP_FRAME_HEIGHT)

area = config["boxes"][0]

print(str(widght) + "x" + str(height))

i = 0
outputpath = sys.argv[2]+"/"
#outputpath = "/home/reth0n/Desktop/videosliced/2/"

bias = max(int(fps/fr), 1)
print("Processing video: "+ sys.argv[1])
while is_opened:
    (flag, frame) = mp4.read()
    
    if flag == True:
        if(i%bias==0):
            mid = [(area[0]+area[2])/2, (area[1]+area[3])/2]
            sca = max(abs(area[0]-area[2]), abs(area[1]-area[3]))/2
            frame = frame[max(int(mid[1]-sca), 1):min(int(mid[1]+sca), height), max(int(mid[0]-sca), 1) : min(int(mid[0]+sca), widght)]            
            file_name = outputpath+"image" + str(i) + ".jpg"
            cv2.imwrite(file_name, frame)  # 保存图片

    else:
    	break
    i+=1

print("Finished")