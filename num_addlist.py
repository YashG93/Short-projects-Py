def num_list(lst):
    return[x+i for x,i in enumerate(lst)]

my_index=[1,2,3,4,5]

print(num_list(my_index))