from PIL import Image
from numpy import *
from numpy import random
from pylab import *
from scipy.ndimage import filters
import imtools
# create synthetic image with noise
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30 * np.random.standard_normal((500,500))
im = array(Image.open('1.jpg').convert('L'))
U,T = imtools.denoise(im,im)
G = filters.gaussian_filter(im,0.5)

figure()
gray()
subplot(1,2,1)
title('ROF denoising')
imshow(U)
subplot(1,2,2)
contour(G, origin='image')
# imshow(G)
title('Gaussian filter')

figure()
gray()
subplot(1,3,1)
imshow(im)
subplot(1,3,2)
imshow(G)
subplot(1,3,3)
imshow(im + (im - G))#un-sharp filtering
show()
