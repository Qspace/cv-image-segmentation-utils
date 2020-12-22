import cv2
import numpy as np
import argparse

binary_threshold_window = 'Global binary thresholding demo'
def binary_threshold(val):
    print(val)
    ret, th = cv2.threshold(
        src, val, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow(binary_threshold_window, th)
    return
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

    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    src = cv2.medianBlur(src, 13)
    cv2.imshow('medianBlur Source Image', src)
    cv2.waitKey(0)

    # Adaptive thresholding on mean and gaussian filter
    th1 = cv2.adaptiveThreshold(
        src, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 11, 2)
    th2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY_INV, 11, 2)
    # Otsu's thresholding
    ret3, th3 = cv2.threshold(
        src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow("th1", th1)
    cv2.waitKey(0)
    cv2.imshow("th2", th2)
    cv2.waitKey(0)
    cv2.imshow("th3", th3)
    cv2.waitKey(0)

    title_track_bar_threshold = 'threshold val'
    cv2.namedWindow(binary_threshold_window)
    cv2.createTrackbar(title_track_bar_threshold,
                    binary_threshold_window, 0, 255, binary_threshold)
    binary_threshold(0)                
    cv2.waitKey(0)