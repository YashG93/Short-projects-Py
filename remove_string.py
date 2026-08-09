
def remove_fun(input_string,index):
    result=[]
    for i in range(1,len(input_string)) :
        if i==index:
            continue
        result+= (input_string[i])
    return ''.join(result)


my_string='Indian Army.'

print(remove_fun(my_string,1))

