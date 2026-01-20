import numpy as np
import vpython as vp

m = 1
k = 6
omega = 2

def f(r, t):
    xr = np.zeros(int(len(r)))
    for i in range(int(len(r)/2)):
        xr[2*i] = r[2*i + 1]
    xr[1] = (k/m)*(xr[2]-xr[0]) + np.cos(omega*t)/m
    for i in range(1, int(len(r)/2)-1):
        xr[2*i + 1] = (k/m)*(xr[2*(i+1)]-xr[2*i]) + (k/m)*(xr[2*(i-1)] - xr[2*i])
    xr[-1] = (k/m)*(xr[-4]-xr[-2])
    return np.array(xr, float)
        

v = np.array([0,0,0,0,0,0,0,0,0,0], float)

tpoints = np.linspace(0, 20, 20000)
xpoints = np.zeros((int(len(v)/2),len(tpoints)))
h = tpoints[1] - tpoints[0]

for ti in range(len(tpoints)):
    for i in range(int(len(v)/2)):
        xpoints[i, ti] = v[2*i]
    k1 = h*f(v, tpoints[ti])
    k2 = h*f(v + 0.5*k1, tpoints[ti] + 0.5*h)
    k3 = h*f(v + 0.5*k2, tpoints[ti] + 0.5*h)
    k4 = h*f(v + k3, tpoints[ti] + h)
    v += (k1 + 2*k2 + 2*k3 + k4)/6


# Make an animation of the masses as they vibrate back and forth

masses = np.array([vp.sphere(pos=vp.vec(2*i, 0, 0), radius=0.2) for i in range(len(xpoints))])

for t in range(len(tpoints)):
    vp.rate(1/h)
    for i in range(len(xpoints)):
        masses[i].pos = vp.vec(2*i + xpoints[i,t],0,0) 
    
