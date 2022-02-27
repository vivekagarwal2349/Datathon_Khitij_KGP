import os
import cv2 as cv
import numpy

dir_path = "/home/krumpr/car-design-generation/thecarconnection_classified_images/pictures/"
folder_name = "left"

for filename in os.listdir(dir_path + folder_name):
    if filename.endswith(".jpg"):
        img = cv.imread(dir_path + folder_name + "/" + filename)
        resized_img = cv.resize(img, (128, 128))
        cv.imwrite(dir_path + "merged" + "/" + filename, resized_img)
        print(filename)