from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('1.jpg').convert('L'))

figure()
gray()
# plot the image
imshow(im)
print 'Please click 3 points'
x = ginput(3)
print 'you clicked:',x
title('original: "1.jpg"')

figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)


show()


