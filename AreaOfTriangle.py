
try:
    base=int(input('Enter the base: '))
    height=int(input('Enter the height: '))
    print(f'The Area of Triangle {0.5 * base * height }')
except ValueError as e:
    print("Enter the Correct value.",e)
