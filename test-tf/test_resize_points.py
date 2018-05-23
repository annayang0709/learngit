
import os
import cv2
from PIL import Image

#010000.jpg 124 155 184 151 152 196 125 223 196 218

def img_landmarks_resize(img_landmarks, width, height, s):
    w = width
    h = height
    l = []
    for i in range(len(img_landmarks)):
        if i % 2 == 0:
            new_x = s * img_landmarks[i] // w
            l.append(int(new_x))
        else:
            new_y = s * img_landmarks[i] // h
            l.append(int(new_y))
    return l


def draw_points(lands, img):
    for i in range(0, len(lands), 2):
        point = (lands[i], lands[i+1])
        cv2.circle(img, point, 1, (255, 0, 0))
        #cv2.imshow('img', img)
    cv2.imwrite('./result_2.jpg', img)
    print('done')

if __name__ == '__main__':

    image = './010002.jpg'
    landmarks = [167, 158, 230, 163, 203, 199, 164, 225, 224, 228]
    img = cv2.imread(image)

    imgl = Image.open(image)
    size = imgl.size
    widthl = size[0]
    heightl = size[1]
    print('width', widthl)
    print('height', heightl)


    width = img.shape[1]
    height = img.shape[0]
    print('img width:', width)
    print('img height:', height)

    img_landmarks = [int(i) for i in landmarks]
    print('landmarks', img_landmarks)
    landmarks_resize = img_landmarks_resize(img_landmarks, width, height, 96)
    print('landmarks_resize', landmarks_resize)
    img = img.resize((96, 96))
    draw_points(landmarks_resize, img)


