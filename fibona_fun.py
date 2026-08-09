def fibo_fun(num):
    a = 0
    b = 1

    for _ in range(num):
        yield a
        a, b = b, a + b

number = int(input("Enter number: "))
print(list(fibo_fun(number)))