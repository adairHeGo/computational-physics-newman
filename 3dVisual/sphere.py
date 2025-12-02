import vpython as vp

#vp.sphere(radius=0.5,pos=vp.vector(1.0,-0.2,0.0), color=vp.color.green)

#L = 5
#R = 0.3

#for i in range(-L, L+1):
#    for j in range(-L, L+1):
#        for k in range(-L, L+1):
#            vp.sphere(pos=vp.vector(i,j,k), radius=R)



#######Exercise 3.4

#a)

L = 5
R = 0.3

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if (i+j+k)%2 !=0:
                vp.sphere(pos=vp.vector(i,j,k), radius=R, color=vp.color.green)
            else:
                vp.sphere(pos=vp.vector(i,j,k), radius=R, color=vp.color.blue)


            
