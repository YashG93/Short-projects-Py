def even_fun(input_num):
    for num in range (input_num+1):
        if num%2==0:
            yield num
        
number=int(input('Enter the number: '))
print(list(even_fun(number)))