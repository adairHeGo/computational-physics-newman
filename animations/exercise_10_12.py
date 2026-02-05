import random as rd
from math import acos,pi,sin,cos
import vpython as vp


for i in range(500):
    vp.rate(10)
    theta = acos(1-2*rd.random())
    phi = 2*pi*rd.random()
    vp.sphere(pos=vp.vector(cos(phi)*sin(theta), sin(phi)*sin(theta),cos(theta)), radius=0.02)
