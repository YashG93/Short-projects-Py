
def list_inte(lst):
    return [ch for ch in lst if isinstance(ch,int)]

my_list=[1,2,'45','Doctor','dgfsdf']
print(list_inte(my_list))