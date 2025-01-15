import torch
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def get_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

path1 = 'E:\\Datasets\\GaoFen-7 dataset\\Train\\image\\Chongqing_8.tif'
path2 = 'E:\\Datasets\\GaoFen-7 dataset\\Train\\label\\Chongqing_8.tif'
img = get_image(path1)
label = get_image(path2)
print(img.shape)
print(label.shape)

plt.figure(figsize=(15, 5))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(label)
plt.show()