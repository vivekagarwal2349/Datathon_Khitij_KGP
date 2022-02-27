import os
import cv2 as cv
import numpy as np

path = "/home/krumpr/car_data/"
folder_name = "front_right128"
i=0
for filename in os.listdir(path + folder_name):
    if i==1000:
        break
    img = cv.imread(path + folder_name + "/" + filename)
    # print(img.shape)
    cv.imwrite("/home/krumpr/Datathon_Khitij_KGP/thecarconnection_classified_images/pictures/merged/"+filename, img)
    i+=1