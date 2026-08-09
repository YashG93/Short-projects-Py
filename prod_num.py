
def pro_num(input_string):
    result=1
    for x in input_string:
        result*=x
    return result

my_string=map(int,input('Enter numbers:').split(','))
print(pro_num(my_string))
 