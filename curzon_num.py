
def curzon_fun(n):
    if (2**n+1)%(2*n+1) ==0:
        return f'{n} is curzon number.'

    return f'{n} is not curzon number.'
    
num=int(input('Enter number: '))
print(curzon_fun(num))
