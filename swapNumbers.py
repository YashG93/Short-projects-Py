try:
   a=int(input('Enter the number a: '))
   b=int(input('Enter the number b: '))
   a,b=b,a

   print(f'value of  a is {a} , value of b is {b}')

except ValueError as v :
   print('Enter the correct input',v)

