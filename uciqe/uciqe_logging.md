# uciqe指标调试记录

opencv转换bgr2lab的异常问题：

[python - cv.COLOR_BGR2LAB gives wrong range - Stack Overflow](https://stackoverflow.com/questions/26992476/cv-color-bgr2lab-gives-wrong-range#:~:text=The%20LAB%20values%20returned%20from,out%20the%208%2Dbit%20range.)

uciqe的github代码仓库：

[GitHub - xueleichen/PSNR-SSIM-UCIQE-UIQM-Python: Python code for several metrics: PSNR, SSIM, UCIQE and UIQM](https://github.com/xueleichen/PSNR-SSIM-UCIQE-UIQM-Python)

[GitHub - Owen718/Image-quality-measure-method: This repository contains frequently used method:UCIQE/UIQM/PSNR/SSIM/MSE by python.](https://github.com/Owen718/Image-quality-measure-method)

[GitHub - TongJiayan/UCIQE-python: Implementation of UCIQE with Python.](https://github.com/TongJiayan/UCIQE-python/tree/main)



安装matlab 的python api：

https://ww2.mathworks.cn/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

根据UCIQE指标所在文献<An Underwater Color Image Quality Evaluation Metric>中使用UIEB的图像结果，实现了UCIQE的代码，由于这个结果与USUIR中的结果不一致，因此我们将我们的评价指标代码进行了开源。

# UIQM指标调试记录




