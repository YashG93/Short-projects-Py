
def div_by(n):
    for num in range(0,n+1):
        if num%5==0 and num%7==0:
            yield num

number=int(input('Enter number range: '))

result=div_by(number)

for num in  result:    
    print(num)
