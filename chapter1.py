from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('1.jpg'))

# plot the image
imshow(im)

# some points
x = [50,100,100,50]
y = [50,50,150,150]

# plot the points with red star-markers
plot(x,y,'r*')

# line plot connecting the first two points
plot(x[:],y[:])

# add title and show the plot
title('Plotting: "1.jpg"')

show()


