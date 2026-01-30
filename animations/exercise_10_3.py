import vpython as vp
import random as rd

L = 101 

i,j = int(L//2 + 1),int(L//2 + 1)

vp.scene.autoscale = False
vp.scene.camera.pos = vp.vec(50,50,0)
vp.scene.center = vp.vec(50,50,0)
vp.scene.range = 70
particle = vp.sphere(pos=vp.vec(i,j,0), radius=1.0)

for n in range(1000000):
    vp.rate(10)
    r = rd.random()
    if i==0:
        if j==0:
            if r<0.5:
                i += 1
            else:
                j += 1
        elif j==L-1:
            if r<0.5:
                i += 1
            else:
                j -= 1
        else:
            if r< 1/3:
                i += 1
            elif r<2/3:
                j += 1
            else:
                j -= 1
    elif i==L-1:
        if j==0:
            if r<0.5:
                i -= 1
            else:
                j += 1
        elif j==L-1:
            if r<0.5:
                i -= 1
            else:
                j -= 1
        else:
            if r< 1/3:
                i -= 1
            elif r<2/3:
                j += 1
            else:
                j -= 1
    if j==0:
        if i==0:
            if r<0.5:
                j += 1
            else:
                i += 1
        elif i==L-1:
            if r<0.5:
                j += 1
            else:
                i -= 1
        else:
            if r< 1/3:
                j += 1
            elif r<2/3:
                i += 1
            else:
                i -= 1
    elif j==L-1:
        if i==0:
            if r<0.5:
                j -= 1
            else:
                i += 1
        elif i==L-1:
            if r<0.5:
                j -= 1
            else:
                i -= 1
        else:
            if r< 1/3:
                j -= 1
            elif r<2/3:
                i += 1
            else:
                i -= 1
    else:
        if r<0.25:
            i += 1
        elif r<0.5:
            i -= 1
        elif r<0.75:
            j += 1
        else:
            j -=1
    particle.pos = vp.vec(i,j,0)
