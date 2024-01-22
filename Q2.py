import librosa
import librosa.display
import cv2 as cv
import numpy as np
import random as rd

height = 300
radius = 25


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



def cvt2rgb(img):
    img_rgb = np.zeros((300,img.shape[1],3),dtype = np.uint8)
    for i in range(300):
        for j in range(img.shape[1]):
            if(img[i,j] != 0):
                x = rd.randint(0,255)
                y = rd.randint(0,255)
                z = rd.randint(0,255)
                img_rgb[i,j] = (x,y,z)
            else:
                img_rgb[i,j] = (0,0,0)  
    
    return img_rgb

def classify_audio(audio_path):

    y, sr = librosa.load(audio_path, sr=None)

    n_fft = 2048  
    hop_length = 512  

    spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft,hop_length=hop_length, fmax=22000)

    spec_db = librosa.power_to_db(spec)

    spec_normalized = cv.normalize(spec_db, None, 0, 255, cv.NORM_MINMAX)

    spec_uint8 = spec_normalized.astype(np.uint8)

    average_intensity = np.mean(spec_uint8)

    threshold = 100

    if average_intensity > threshold:
        return(1)
    else:
        return(2)


sum = 0
test_files = []

for i in range(len(test_files)):
    audio_file = test_files[i]
    sum += classify_audio(audio_file)

sum = str(sum)

sum_len = int(len(sum))

image = np.zeros((300, sum_len*200), dtype=np.uint8)

index = 0

for i in range(sum_len):
    a = int(sum[i])
    add_to_matrix(image, index, a)
    if a != 1:
        index += 200
    else :
        index += 100
    
img_rgb = cvt2rgb(image)

cv.imshow('RGB image', img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()

