import random as rd
import numpy as np
import vpython as vp

L = 101 
grid = np.zeros((L,L), int)
spheres = []
k = 0
while grid[50,50]==0:
    i,j = 50,50
    spheres.append(vp.sphere(pos=vp.vector(i,j,0), color=vp.color.white))
    while True:
        vp.rate(1000)
        r = rd.random()
        if i==0 or j==0 or i==100 or j==100:
            grid[i,j] = 1
            spheres[k].color = vp.color.cyan
            break
        elif grid[i+1,j]== 1 or grid[i-1,j]==1 or grid[i,j+1]==1 or grid[i,j-1]==1:
            grid[i,j] = 1
            spheres[k].color = vp.color.cyan
            break
        else:
            if r<0.25:
                i += 1
            elif r<0.5:
                i -= 1
            elif r<0.75:
                j += 1
            else:
                j -=1
            spheres[k].pos = vp.vector(i,j,0)
    k += 1
                
