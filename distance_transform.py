import numpy as np
import cv2
import argparse

title_erosion_window = 'Otsu thresholding Demo'
title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
dist = None
def thresholding(val):
    val = float(val/100)
    print(val)
    global dist
    tmp_dist = None
    for _ in range(10):
        # Threshold to obtain the peaks
        # This will be the markers for the foreground objects
        _, tmp_dist = cv2.threshold(dist, val, 1.0, cv2.THRESH_BINARY)
        # Dilate a bit the dist image
        kernel1 = np.ones((3,3), dtype=np.uint8)
        tmp_dist = cv2.dilate(tmp_dist, kernel1)
    cv2.imshow(title_erosion_window, tmp_dist)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Image Segmentation with Distance Transform and Watershed Algorithm.\
        Sample code showing how to segment overlapping objects using Laplacian filtering, \
        in addition to Watershed and Distance Transformation')
    parser.add_argument('--input', help='Path to input image.',
                        default='cards.png')
    args = parser.parse_args()
    src = cv2.imread(cv2.samples.findFile(args.input),0)
    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)
    # Show source image
    cv2.imshow('Source Image', src)
    cv2.waitKey(0)

    # Perform the distance transform algorithm
    dist = cv2.distanceTransform(src, cv2.DIST_L2, 3)
    # Normalize the distance image for range = {0.0, 1.0}
    # so we can visualize and threshold it
    cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
    cv2.imshow('Distance Transform Image', dist)
    cv2.waitKey(0)

    cv2.namedWindow(title_erosion_window)
    cv2.createTrackbar(title_trackbar_kernel_size,
                    title_erosion_window, 0, 100, thresholding)
    thresholding(0)
    cv2.waitKey(0)