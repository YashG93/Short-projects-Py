
def bin_fun(input_str):
    for i in input_str:
        if i not in '10':
            return False
    return True
    
my_string='10010'

if bin_fun(my_string):
    print(f'{my_string} is binary.')
else:
    print(f'{my_string} is not binary.')