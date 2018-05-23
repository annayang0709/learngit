import cv2
import os

def face_detectoe(img_path):
    image = cv2.open(img_path)
    Grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(‘haarcascade_frontalface_default.xml’)
    bounding_boxes = face_cascade.detectMultiScale(Grayscale_image, 1.25, 6)


