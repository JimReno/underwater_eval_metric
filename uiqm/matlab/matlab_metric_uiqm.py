# import psnr
# import ssim
import os
import sys
import cv2
import scipy.misc
import numpy
import numpy as np
import matlab.engine
import cv2
# import imgqual_utils
from PIL import Image

#author：yetian
#time：2020/12/7


dist_path = "m906_img_.png"
def cv_show(img,name):
    cv2.imshow(img,name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

save_file = '906_img.txt'

uciqe_list = []

eng = matlab.engine.start_matlab()


uiqm_data = eng.main_metric(dist_path)
print(uiqm_data)