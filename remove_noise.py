import matplotlib.pyplot as plt
import os
import cv2
import numpy as np

data_path = "dataset/"
img_filenames = os.listdir(data_path)
images = []
for filename in img_filenames:
    img_path = os.path.join(data_path, filename)
    img = plt.imread(img_path)
    
    # Remove noise from the image
    height, width = img.shape[0:2]
    for i in range(0, height):
        for j in range(0, width):
            if (img[i][j][3] <= .34 or (
                    (img[i][j][2] * 255 > 170) and (img[i][j][1] * 255 > 150) and (img[i][j][0] * 255 > 150))):
                img[i][j] = 0

    kernel = np.ones((3, 3), np.float32) / 9
    img = cv2.filter2D(img, -1, kernel)

    for i in range(0, height):
        for j in range(0, width):
            if (img[i][j][3] <= .30 or (
                    (img[i][j][2] * 255 > 170) and (img[i][j][1] * 255 > 150) and (img[i][j][0] * 255 > 150))):
                img[i][j] = 0

    # Save and display the cleaned image
    plt.imshow(img)
    plt.savefig("cleaned_" + filename)
    plt.show()