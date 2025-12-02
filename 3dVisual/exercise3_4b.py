import vpython as vp

#######Exercise 3.4

#b)

L = 3
R = 0.2

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            vp.sphere(pos=vp.vector((i+j)/2,(j+k)/2,(k+i)/2), radius=R)
            
