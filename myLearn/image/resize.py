import PIL
from PIL import Image
img = Image.open('E:\\git\\mdn-learning-area\\html\\multimedia-and-embedding\\mdn-splash-page-start\\originals\\red-panda.jpg')
print(img.size)
print(type(img.size))
size = (600,img.size[1])
out = img.crop(box = (650,0,1250,img.size[1]))
out.save(r'E:\git\mdn-learning-area\html\multimedia-and-embedding\mdn-splash-page-start\originals\red-panda_600pxw.jpg')
img.close()