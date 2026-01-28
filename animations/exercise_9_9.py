import numpy as np
import vpython as vp
from dcst import dst,idst

L = 1e-8
N = 1000
a = L/N
h = 1e-18
m = 9.109e-31
x0 = L/2
sigma = 1e-10
kappa = 5e10
hbar = 1.054571817e-34

psir = np.empty(N+1, float)
psii = np.empty(N+1, float)
psir[0] = 0
psii[N] = 0
psir[0] = 0
psii[N] = 0
for i in range(1,N):
    psir[i] = np.exp(-((i*a - x0)**2)/(2*sigma**2))*np.exp(1j*sigma*i*a).real
    psii[i] = np.exp(-((i*a - x0)**2)/(2*sigma**2))*np.exp(1j*sigma*i*a).imag
    
alpha = dst(psir)
eta = dst(psii)

def wavef(t):
    coeff = np.empty(N+1, float)
    for i in range(N+1):
        coeff[i] = alpha[i]*np.cos(t*np.pi**2*hbar*i**2/(2*m*L**2)) -eta[i]*np.sin(t*np.pi**2*hbar*i**2/(2*m*L**2))
    return idst(coeff)


t = 0
tf = 1e-14

psi_t = wavef(0)
points = [vp.sphere(pos=vp.vec(i,500*psi_t[i],0), radius=5) for i in range(N+1)]

#pp = vp.sphere(pos=vp.vec(0,0,0), radius=10)

while t<tf:
    vp.rate(100)
    psi_t = wavef(t)
    for i in range(N+1):
        points[i].pos = vp.vec(i,500*psi_t[i],0)
    t += h
