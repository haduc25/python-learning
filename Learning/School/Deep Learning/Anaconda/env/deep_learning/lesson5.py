# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:54:49 2023

@author: Admin
"""

# 3. Xây dựng chương trình thực hiện sải bước (Stride) trong ảnh.
import cv2
import numpy as np

# func
def apply_sliding_window(img, kernel, padding=0, stride=1):
    h, w = img.shape[:2]
    
    img_p = np.zeros([h+2*padding, w+2*padding])
    img_p[padding:padding+h, padding:padding+w] = img
    
    kernel = np.array(kernel)
    assert len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1] # square kernel
    assert kernel.shape[0] % 2 != 0 # kernel size is odd number

    k_size = kernel.shape[0]
    k_half = int(k_size/2)
    
    y_pos = [v for idx, v in enumerate(list(range(k_half, h-k_half))) if idx % stride == 0]
    x_pos = [v for idx, v in enumerate(list(range(k_half, w-k_half))) if idx % stride == 0]
    
    new_img = np.zeros([len(y_pos), len(x_pos)])
    for new_y, y in enumerate(y_pos):
        for new_x, x in enumerate(x_pos):
            if k_half == 0:
                pixel_val = img_p[y, x] * kernel # element-wise multiply
            else:
                pixel_val = np.sum(img_p[y-k_half:y-k_half+k_size, x-k_half:x-k_half+k_size] * kernel) # dot product: https://minhng.info/toan-hoc/y-nghia-tich-vo-huong.html
            new_img[new_y, new_x] = pixel_val
    
    return new_img

def apply_sliding_window_on_3_channels(img, kernel, padding=0, stride=1):
    layer_blue = apply_sliding_window(img[:,:,0], kernel, padding, stride)
    layer_green = apply_sliding_window(img[:,:,1], kernel, padding, stride)
    layer_red = apply_sliding_window(img[:,:,2], kernel, padding, stride)
    
    new_img = np.zeros(list(layer_blue.shape) + [3])
    new_img[:,:,0], new_img[:,:,1], new_img[:,:,2] = layer_blue, layer_green, layer_red
    return new_img
 
    
# import image
image = cv2.imread('../img/img2.jpg')  

# Print error message if image is null
if image is None:
    print('Could not read image')


new_img = apply_sliding_window_on_3_channels(image, kernel=[[1]], padding=0, stride=2)
cv2.imwrite('../imgExported/imgNew.jpg', new_img)

    
lighten_blur_img = apply_sliding_window_on_3_channels(image, kernel=[[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]], padding=1, stride=1)
cv2.imwrite('../imgExported/imagelightenBlur.jpg', lighten_blur_img)
print('Success!')

cv2.waitKey()
