from PIL import Image

imageName="5"
im = Image.open(imageName+'.png')
im.save(imageName+'.png')