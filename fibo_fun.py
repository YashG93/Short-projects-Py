def fibo_fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo_fun(n-1)+fibo_fun(n-2)


num=int(input(' Fibonacci sereis up to LIMIT:'))
for i in range(num):
    print(fibo_fun(i),end=" ")

