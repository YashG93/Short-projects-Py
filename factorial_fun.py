
def fact_fun(n):
    if n==1:
        return 1
    else:
        return n* fact_fun(n-1)
    
num=int(input('Enter factorial of : '))
print(fact_fun(num))











    