import numpy as np
import cv2

def getUCIQE(img):
    img_BGR = cv2.imread(img)
    img_BGR_float = img_BGR.astype("float32") / 255
    # hsv_image = cv2.cvtColor(img_BGR_float, cv2.COLOR_BGR2HSV)  
    img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB) 
    img_LAB = np.array(img_LAB,dtype=np.float32)
    # Trained coefficients are c1=0.4680, c2=0.2745, c3=0.2576 according to paper.
    coe_Metric = [0.4680, 0.2745, 0.2576]
    

    img_lum = img_LAB[:,:,0]/255.0
    img_a = img_LAB[:,:,1]/255.0
    img_b = img_LAB[:,:,2]/255.0

    # item-1
    chroma = np.sqrt(np.square(img_a)+np.square(img_b))
    sigma_c = np.std(chroma)

    # item-2
    img_lum = img_lum.flatten()
    img_lum_sort = np.sort(img_lum)
    length = len(img_lum_sort)  
    index_1_percent = int(np.round(length * 0.010))  
    index_last_1_percent = int(np.round(length * 0.990)) 
    bottom_pixels = img_lum_sort[:index_1_percent]
    top_pixels = img_lum_sort[index_last_1_percent:]
    con_lum = top_pixels.mean() - bottom_pixels.mean()

    # item-3
    chroma = chroma.flatten()
    sat = np.divide(chroma, img_lum, out=np.zeros_like(chroma, dtype=np.float64), where=img_lum!=0)
    avg_sat = np.mean(sat)


    print(sigma_c, con_lum, avg_sat)
    uciqe = sigma_c*coe_Metric[0] + con_lum*coe_Metric[1] + avg_sat*coe_Metric[2]
    return uciqe

if __name__ == '__main__':
    img = 'm906_img_.png'
    uciqe = getUCIQE(img)
    print("UCIQE of image '{0}' = {1}".format(img,uciqe))