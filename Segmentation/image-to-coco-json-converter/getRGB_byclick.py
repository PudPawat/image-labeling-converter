import cv2
import numpy as np

global colors, coord
def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        coord = (x,y)

        print("({})".format(colors))
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

        cv2.putText(image, str(colors), coord, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)




# Read an image, a window and bind the function to window
# image = cv2.imread("./dataset/lunar/mock_sim/raw/1_499.png")
image = cv2.imread("F:\Lunar thailand\CODE\Segmentation\image-to-coco-json-converter\dataset\simtest\\1000_11536.png")
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#Do until esc pressed
while(1):

    cv2.imshow('mouseRGB',image)

    if cv2.waitKey(20) & 0xFF == 27:
        break

#if esc pressed, finish.
cv2.destroyAllWindows()