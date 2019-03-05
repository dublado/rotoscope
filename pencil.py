import imageio,numpy as np,scipy.ndimage, matplotlib.pyplot as plt
from urlparse import urlparse 
from PIL import Image
import os
from os.path import splitext, basename

def dodge(front,back):
    v=255
    result=front*v/(v-back) 
    result[result>v]=v
    result[back==v]=v
    return result.astype('uint8')

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def geraha(img):   
    fn = urlparse(img)
    filename, ext = splitext(basename(fn.path))

    print(filename + " " + ext)
    s = imageio.imread(img)
    g = grayscale(s)
    i = 255-g
    b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    r = dodge(b,g)
    plt.imshow(r, cmap="gray")
    final_file = filename + ".png"
    plt.imsave(final_file, r, cmap='gray', vmin=0, vmax=255)
    img = Image.open(final_file)
    file_out = filename + ".bmp"
    img.save(file_out)
    os.remove(final_file)


import sys
geraha(sys.argv[1])
