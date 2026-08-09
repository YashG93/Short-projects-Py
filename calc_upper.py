
def upper_ele(in_string):
    posi=[]
    result=[]
    for lett in in_string:
        if lett.isupper():
            posi.append(in_string.index(lett))
            result.append(lett)
    return result,posi

my_string="HeLlo"
print(upper_ele(my_string))

