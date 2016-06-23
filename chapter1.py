from PIL import Image
from pylab import *
from imtools import *

# read image to array
im = array(Image.open('1.jpg').convert('L'))


figure()
gray()
imshow(im)

figure()
gray()
im = array(Image.open('1.jpg').convert('L'))
im2,cdf = histeq(im)
imshow(im2)

figure()
gray()
# plot the image
imshow(im[60:100,:])
print 'Please click 3 points'
x = ginput(3)
print 'you clicked:',x
print im.shape, im.dtype
title('original: "1.jpg"')

figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)


show()


