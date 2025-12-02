import vpython as vp
from math import cos, sin, pi
from numpy import arange, array

#s = vp.sphere(pos=vp.vec(1,0,0), radius=0.1)

#for theta in arange(0, 10*pi, 0.1):
#    vp.rate(30)
#    x = cos(theta)
#    y = sin(theta)
#    s.pos = vp.vec(x,y,0)   

#Exercise 3.5

c1 = 3

Sun = vp.sphere(pos=vp.vec(0,0,0), radius=50000, color=vp.color.yellow)
Mercury = vp.sphere(pos=vp.vec(57900,0,0), radius=c1*2440, color=vp.color.green)
Venus = vp.sphere(pos=vp.vec(108200,0,0), radius=c1*6052)
Earth = vp.sphere(pos=vp.vec(149600,0,0), radius=c1*6371, color=vp.color.blue)
Mars = vp.sphere(pos=vp.vec(227900,0,0), radius=c1*3386, color=vp.color.red)
Jupiter = vp.sphere(pos=vp.vec(778500,0,0), radius=c1*69173)
Saturn = vp.sphere(pos=vp.vec(1433400,0,0), radius=c1*57316)

Planets = array([Mercury, Venus, Earth, Mars, Jupiter, Saturn])

Orbits_rad = array([57900, 108200, 149600, 227900, 778500, 1433400])
Periods = array([88.0,224.7,365.3,687.0,4331.6,10759])

for theta in arange(0, 1000*pi, 0.1):
    vp.rate(1000)
    for i in range(len(Planets)):
        x = cos(2*pi*theta/Periods[i])
        y = sin(2*pi*theta/Periods[i])
        Planets[i].pos = vp.vec(Orbits_rad[i]*x, Orbits_rad[i]*y, 0)

