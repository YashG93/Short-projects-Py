
def hars_fun(n):
    if n% ((n%10)+(n//10))==0:
        print('Harshad Number.')
    else:
        print('Not a Harshad Number.')


num=int(input('Enter number: '))
print(f'{hars_fun(num)}')












