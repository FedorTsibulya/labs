import numpy as np
import imageio as im

image_origin = im.imread_v2('useful.jfif')
gray = np.array([0.299, 0.587, 0.114])
image_gray = np.dot(image_origin, gray)
im.imwrite('more_useful.png', image_gray)