
def order_lst(inp_string):
    return  inp_string ==''.join(sorted(inp_string))

my_string=input("Enter String: ")
print(order_lst(my_string))
