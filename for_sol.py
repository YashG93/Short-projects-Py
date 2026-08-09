from math import sqrt
def form_fun(d):
    return round(sqrt((2*50*d)//30))

val=int(input('Enter value of d: '))
print(f'{form_fun(val)}')



