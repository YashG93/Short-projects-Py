
def add(num1,num2):
    print(f'Addition is {num1+num2}')

def sub(num1,num2):
    print(f'Substraction is {num1-num2}')

def mult(num1,num2):
    print(f'Multiplicatioin is {num1*num2}')

def div(num1,num2):
    print(f'Division is {num1/num2}')

num1=int(input('Enter number: '))
num2=int(input('Enter number: '))


choice=int(input(' 1)Addition: \n 2)Substraction: \n 3)Multiplication: \n 4)Division: \n Enter Choice:'))

match choice:
    case 1: add(num1,num2)
    case 2: sub(num1,num2)
    case 3: mult(num1,num2)
    case 4: div(num1,num2)
    case _: print("Enter valid choice.")






