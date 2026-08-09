
try:
    year=int(input('enter the Year: '))
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f'{year} is a Leap Year.')

    else:
        print(f'{year} is not Leap Year.')
    
except ValueError :
    print('Enter  correct YEAR.')