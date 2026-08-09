
print("Welcome to the Simple Calculator by the python")
while True:
    try:
      number1=float(input("Enter number: "))
      number2=float(input("Enter another number: "))
      break
    except ValueError :
      print("Enter correct numbers")
    
op=input("Enter operator +,-,*,/: ")
 
if op=='+':
    print(f'Addition of {number1} and {number2} is {number1+number2}')

elif op=='-':
    print(f"Substraction of {number1} and {number2} is {number1-number2}")

elif op=='*':
    print(f'Multiplication of the {number1} and {number2} is {number2*number1}')

elif op=='/' :
    print(f'Division of the {number1} and {number2} is {number1/number2}')

else :
    print('please enter correct operators')



