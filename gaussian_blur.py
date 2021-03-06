import cv2
import numpy as np
import argparse

gausian_blur_window = 'Global binary thresholding demo'

def gaussian_blur(val):
    dst = cv2.GaussianBlur(src, 2*val+1)
    cv2.imshow(gausian_blur_window, dst)
    cv2.waitKey(0)
    return

src = None
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='gausian blur')
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
    title_track_bar_threshold = 'kernel size 2n+1'
    cv2.namedWindow(gausian_blur_window)
    cv2.createTrackbar(title_track_bar_threshold,
                    gausian_blur_window
            , 0, 10, gaussian_blur)
    gaussian_blur(0)