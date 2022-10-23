import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os
import json

"""
The class is to extract the outline from a picture, 
help the image classification to get the feature.
img: image to be handled with.

img_gamma: image after gamma correction.
gradient: image after morphology.
closing: image after closing.
"""

class outlineExtractor:
    def __init__(self, img): # Initial the class
        self.img = img
        self.img_gamma = []
        self.gradient = []
        self.closing = []

    def gammaCorrection(self, gammaRate = 0.7): # adjust the level of gamma, default = 0.7
        print("Start gamma correction...")
        # convert img to gray
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # compute gamma = log(mid*255)/log(mean)
        mid = gammaRate
        mean = np.mean(gray)
        gamma = math.log(mid*255)/math.log(mean)
        # do gamma correction
        self.img_gamma = np.power(self.img, gamma).clip(0,255).astype(np.uint8)
    def morphology(self, kernal_size = (3,3)): # adjust kernal size, decide the datail the aglorithm use.
        print("Start to get the outline...")
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernal_size)
        self.gradient = cv2.morphologyEx(self.img_gamma, cv2.MORPH_GRADIENT, kernel)
        self.closing = cv2.morphologyEx(self.gradient, cv2.MORPH_CLOSE, kernel, iterations=10)