from urllib2 import urlopen
from PIL import Image
url1 = 'https://www.nvidia.com/content/dam/en-zz/Solutions/intelligent-machines/jetson-nano/nvidia-jetson-nano-module-standing-1cc-d.jpg'
fileToSave = urlopen(url1)
image = Image.open(fileToSave)
image.save('images\\original.jpg')
half = (image.size[0]/2, image.size[1]/2)
half_image1 = image.resize(half, Image.ANTIALIAS)
half_image1.save('images\\half.jpg')
rot1 = image.transpose(Image.ROTATE_90)
rot1.save('images\\r90.jpg')
rot2 = image.transpose(Image.ROTATE_180)
rot2.save('images\\r180.jpg')
rot3 = image.transpose(Image.ROTATE_270)
rot3.save('images\\r270.jpg')
