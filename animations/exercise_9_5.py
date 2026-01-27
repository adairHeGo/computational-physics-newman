import numpy as np
import matplotlib.pyplot as plt
import vpython as vp

v = 100
L = 1
d = 0.1
C = 1
sigma = 0.3
h = 1e-6
N = 100
a = L/N
epsilon = h/1000

tend = 50e-3
t1 = 1e-5
t2 = 1e-4
t3 = 1e-3
t4 = 15e-3

T = np.empty(N+1, float)
T[:] = 0 
Tp = np.empty(N+1, float)
for i in range(N+1):
    Tp[i] = C*(a*i)*(L-a*i)*np.exp(-(a*i -d)**2/(2*sigma**2))/(L**2) 
T2 = np.empty(N+1,float)
T3 = np.empty(N+1,float)

t = 0.0
c = h*(v**2)/(a*a)

#We define the spheres as each point in the string.
points_string = [vp.sphere(pos=vp.vec(i,100000*T[i],0)) for i in range(N+1)]

while t<tend:
    T2[1:N] = T[1:N] + h*Tp[1:N]
    T3[1:N] = Tp[1:N] + c*(T[0:N-1] + T[2:N+1] - 2*T[1:N])
    T2,T = T,T2
    Tp,T3 = T3,Tp
    t += h
    vp.rate(10000)
    for i in range(N+1):
        points_string[i].pos = vp.vec(i,100000*T[i],0)
    
