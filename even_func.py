def even_fun(n):
    return [x for x in range(n+1) if x%2==0]

input_num=int(input('Enter number: '))
print(even_fun(input_num))