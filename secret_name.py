def sec_name(inp_lst):
    sect_name=''.join(sorted(name[0] for name in inp_lst))
    return sect_name

my_list=list(input('Enter names: ').split(','))
print(sec_name(my_list))