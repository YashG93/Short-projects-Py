import math
def  degree(n):
     return (180/math.pi)*n

radian=float(input('Enter radian: '))
print(f'{radian} Radian is {degree(radian):.2f} degree.')
