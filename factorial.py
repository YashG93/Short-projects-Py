
num=int(input('Factorial of : '))
if num>0:
    j=1
    for i in range(2,num+1):
        j=j*i
    print(f'Factorial of {num} is {j}')

else:
    print(f'No factorial for {num}')