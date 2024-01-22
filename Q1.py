import cv2 as cv
import numpy as np


height = 300
radius = 25

def toh(n):
    if n<=0 :
        return 0
    else :
        return 2**n-1

def add_to_matrix(img, index, a):
    if(a == 0):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50,  100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 200), radius = radius, color = 255, thickness = -1)
    elif(a == 1):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
    elif(a == 2):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
    elif(a == 3):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
    elif(a == 4):
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 100), radius = radius, color = 255, thickness = -1)
    elif(a == 5):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50,  100), radius = radius, color = 255, thickness = -1)   
    elif(a == 6):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50,  100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 200), radius = radius, color = 255, thickness = -1)     
    elif(a == 7):
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
    elif(a == 8):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50,  100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 200), radius = radius, color = 255, thickness = -1)
    elif(a == 9):
        cv.circle(img, (index + 50, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 50), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 100), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 150), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 200), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 100, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 150, 250), radius = radius, color = 255, thickness = -1)
        cv.circle(img, (index + 50,  100), radius = radius, color = 255, thickness = -1)
    

n = int(input("Enter the no of disk: "))
n = toh(n)

n = str(n)

n_len = int(len(n))

image = np.zeros((300, n_len*200), dtype=np.uint8)

index = 0

for i in range(len(n)):
    a = int(n[i])
    add_to_matrix(image, index, a)
    if a != 1:
        index += 200
    else :
        index += 100
    

cv.imshow('img', image)

cv.waitKey(0)
cv.destroyAllWindows()