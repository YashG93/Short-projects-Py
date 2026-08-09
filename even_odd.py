try:
    num=int(input('Enter value: '))
    
    if num==0:
        print('Number is 0.')

    elif num%2!=0:
        print(f'{num}is odd number.')

    else:
        print(f'{num} is even number.')

except ValueError as v:
    print('Enter the correct value.',v)

