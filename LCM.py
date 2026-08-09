import math

num_1=int(input('Enter number: '))
num_2=int(input('Enter number: '))

lcm=(num_1*num_1)//math.gcd(num_1,num_2)

print('LCM',lcm)
