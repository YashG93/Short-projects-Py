num=int(input('Enter Fibonacci upto : '))
a=0
b=1

for i in range (0,num):
    print(a)
    c=a+b
    b=a
    a=c

