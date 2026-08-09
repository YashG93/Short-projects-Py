
def cube_fun(n):
    if n==0:
        return 0

    elif n>0:
        return n**3 + cube_fun(n-1)

num=int(input('Enter number upto: '))
if num<=0:
    print('Enter number greater than 0.')
else:
    print(f'Cube of 0 to {num} is {cube_fun(num)}. ')
