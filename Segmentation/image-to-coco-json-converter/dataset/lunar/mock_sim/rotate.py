import cv2
import os

path = "./seg_copy"
listname = os.listdir(path)



for name in listname:

    im = cv2.imread(os.path.join(path,name))

    im = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)

    im = cv2.imwrite(os.path.join(path,name), im)


