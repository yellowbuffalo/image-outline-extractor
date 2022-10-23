import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import json
from outlineExtractor import *
path_folder_test = './data'
os.chdir(path_folder_test) # Setting data path
list_img = os.listdir() # Get all img as a list from the file.
os.chdir('../') # recover the path

print(list_img) # Check the example data.

# Start to handle every image and output the outline image.
for target in list_img:
    print("Now ", target, ' ...')
    path = './data/' + target
    img = cv2.imread(path)
    img_process = outlineExtractor(img) # Implement the class on image.
    img_process.gammaCorrection() # Conduct the gamma correction to brighten the picture.
    img_process.morphology() # Doing morphology to outline the image.
    cv2.imwrite('./output/gamma/' + target, img_process.img_gamma)  # Output the img after gamma
    cv2.imwrite('./output/outline/' + target, img_process.gradient) # Output the outline
    cv2.imwrite('./output/closing/' + target, img_process.closing)  # Output the img after closing
    print('---end---')