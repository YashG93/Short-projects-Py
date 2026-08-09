try:
    num=int(input('Enter number: '))

    if num>0:
      print(f'{num} is positive number.')
    
    elif num<0:
       print(f'{num} is negative number.')
     
    else :
       print('Number is 0')
    
except ValueError as v:
   print('Enter correct Input.',v)
