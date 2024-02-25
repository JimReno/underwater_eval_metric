## UIQM and UCIQE
This repository contains several image quality evaluation metric:
- UIQM
- UCIQE

Although many repositories have implemented UIQM and UCIQE, there are some errors in the code or the metrics are implemented by matlab. So the author referenced all the repositories from web and re-implemented these two metric. The evaluation image is a raw image from '906_img_.png' from UIEB dataset.

The UIQM metric mainly reference owen's code from: https://github.com/Owen718/Image-quality-measure-method/

The UCIQE metric mainly use TongJiayan's code from: https://github.com/TongJiayan/UCIQE-python



Metrics including SSIM and PSNR have already implemented by sklearn. Try to calculate SSIM and PSNR using the snippet below:

```python
import numpy as np  
from skimage.measure import compare_psnr, compare_ssim  
  
def calculate_psnr(img1, img2):  
    # img1 and img2 have range [0, 255]  
    img1 = img1.astype(np.float64)  
    img2 = img2.astype(np.float64)  
    mse = np.mean((img1 - img2)**2)  
    if mse == 0:  
        return float('inf')  
    return 20 * np.log10(255.0 / np.sqrt(mse))  


# example 
img1 = np.random.randint(0, 256, (5, 5), dtype=np.uint8)  
img2 = np.random.randint(0, 256, (5, 5), dtype=np.uint8)  
  
print(calculate_psnr(img1, img2))
```

## Todo
- Add more underwater image evaluation metrics.

## referenced pages:
https://github.com/Owen718/Image-quality-measure-method/
https://github.com/TongJiayan/UCIQE-python

