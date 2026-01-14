import numpy as np
import matplotlib.pyplot as plt
import vpython as vp

g = 9.81
l = 0.1

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta)
    return np.array([ftheta,fomega], float)


v = np.array([(np.pi/180)*179, 0], float)

tpoints = np.linspace(0, 50, 1000)
thetapoints = []
h = tpoints[1] - tpoints[0]

for t in tpoints:
    thetapoints.append(v[0])
    k1 = h*f(v, t)
    k2 = h*f(v + 0.5*k1, t + 0.5*h)
    k3 = h*f(v + 0.5*k2, t + 0.5*h)
    k4 = h*f(v + k3, t + h)
    v += (k1 + 2*k2 + 2*k3 + k4)/6

#Animation

mass = vp.sphere(pos=vp.vec(l*np.sin(np.pi*179/180), -l*np.cos(np.pi*179/180), 0), radius=0.01) 

for t in range(1, len(tpoints)):
    vp.rate(1/h)
    mass.pos = vp.vec(l*np.sin(thetapoints[t]), -l*np.cos(thetapoints[t]), 0)
    
