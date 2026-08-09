import math

def cone_vol(h,r):
    if r==0:
        return 0
    volume=(1/3)*math.pi*(r**2)*h
    return round(volume,2)

height,radius=map(float,input('Enter Height and Radius respectively: ').split(','))
print(cone_vol(height,radius))