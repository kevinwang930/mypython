# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:50:14 2020

@author: kevin
"""


from PIL import Image, ImageFilter
 
if __name__=="__main__":
    im = Image.open("test.jpg")
 
kernelValues = [-1,-1,-1,-1,8,-1,-1,-1,-1] #emboss
#kernel = ImageFilter.Kernel((3,3), kernelValues)
#kernel = ImageFilter.FIND_EDGES
im2 = im.filter(ImageFilter.FIND_EDGES)

im2.save("test-out.jpg")
im2.show()