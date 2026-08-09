##IS even or odd
# def is_odd(n):
#     if n<2:
#         return False
#     elif n%2==0:
#         print(f'number {n} is even number')
#     else:
#         print(f'number {n} is prime number')
        

# while True:
#     try:
#         is_odd(int(input("Enter number: ")))
#     except ValueError:
#         raise("Enter correct number")
    
## Is prime

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    print (f'{n} is prime number')

is_prime(int(input('Enter number')))