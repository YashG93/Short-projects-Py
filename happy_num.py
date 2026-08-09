
num=int(input('Enter number: '))

while num!=1 and num!=4 :
    s=0
    while num>0:
        digit=num%10
        s=s+digit*digit
        num=num//10
    num=s

if num==1:
    print("Happy Number.")
else :
    print('Not a Happy Number.')












