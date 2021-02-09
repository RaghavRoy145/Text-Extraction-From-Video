from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
import os
import cv2

#create directory for frames
if not os.path.exists('image_frames'):
    os.makedirs('image_frames')

#create video path for sample video
test_vid=cv2.VideoCapture('testvideo.mp4')

#start index for frames
index=0
while test_vid.isOpened():
    ret,frame=test_vid.read()
    if not ret:
        break
    
#assign name to the files
    name='./image_frames/frame'+str(index)+'.png'
    print('Extracting frames...' + name)
    cv2.imwrite(name, frame)
    index+=1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    test_vid.release()
    cv2.destroyAllWindows()

print("text from video...")

#using just the first frame, can be changed to multiple by adding a loop
demo= Image.open("./image_frames/frame0.png")
text=pytesseract.image_to_string(demo, lang='eng')
print(text)


