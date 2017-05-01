# -*- coding:utf-8 -*-

import numpy as np
from PIL import Image


im=np.array(Image.open("sea.jpg").convert('L'))
depth=10
grad=np.gradient(im)
grad_x,grad_y=grad
grad_y=grad_y*depth/100
vec_el=np.pi/2.2
vec_az=np.pi/4
dx=np.cos(vec_el)*np.cos(vec_az)
dy=np.cos(vec_el)*np.sin(vec_az)
dz=np.sin(vec_el)
a=np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x=grad_x/a
uni_y=grad_y/a
uni_z=1./a
b=255*(dx*uni_x + dy*uni_y + dz*uni_z)
b.clip(0,255)
hand_im=Image.fromarray(b.astype('uint8'))
hand_im.save('hand_im.jpg')
