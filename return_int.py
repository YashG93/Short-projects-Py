
def ret_num(input_string):
    return [x for x in input_string if  x.strip().isdigit()]

my_string=input('Enter string: ').split(',')
print(ret_num(my_string))
