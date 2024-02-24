# import psnr
# import ssim
import os
import sys
import cv2
import scipy.misc
import numpy
import uqim_utils
import numpy as np
import matlab.engine
import cv2
# import imgqual_utils
from PIL import Image

#author：yetian
#time：2020/12/7


dist_path = r"D:\\workspace\\python\\uie-metric\\uciqe\\m906_img_.png"
def cv_show(img,name):
    cv2.imshow(img,name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# dist_filelist = os.listdir(dist_path) #测试图像文件列表
dist_filelist = [dist_path] #测试图像文件列表

save_file = '906_img.txt'

uciqe_list = []

eng = matlab.engine.start_matlab()
for dist_file in dist_filelist: #遍历
    dist_file_dir = os.path.join(dist_path,dist_file) #文件绝对路径
    
    if os.path.isdir(dist_file_dir): #如果是文件夹，跳过
        continue 



    uciqe_data = eng.test_UCIQE2py(dist_file_dir)
    
    filename = dist_file
    print("img:" + str(filename)+" UCIQE:"+str(uciqe_data))
    data = str(filename)+" UCIQE:"+str(uciqe_data)
    

    uciqe_list.append(uciqe_data)


    average = " UCIQE average:"+str(sum(uciqe_list)/len(uciqe_list)) 
    print(average)
    if uciqe_data>0.65:
        with open(save_file,"a") as file:
            file.write(data + " "+average +'\n')