from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('1.jpg').convert('L'))
#Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

figure()
gray()
subplot(2,2,1)
imshow(im)
subplot(2,2,2)
imshow(imx)
subplot(2,2,3)
imshow(imy)
subplot(2,2,4)
imshow(imx + imy)


sigma = 1 #standard deviation
imxG = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (0,1), imxG)
imyG = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (1,0), imyG)
figure()
gray()
subplot(2,2,1)
imshow(im)
subplot(2,2,2)
imshow(imxG)
subplot(2,2,3)
imshow(imyG)
subplot(2,2,4)
print  int(imxG.min()), int(imxG.max()), int(imyG.min()), int(imyG.max())
im_thresh = 1 * ((abs(imx) + abs(imy)) < 120)

imshow(im_thresh)
show()
