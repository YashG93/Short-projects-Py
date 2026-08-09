
def count_fun(l,element):
    count=l.count(element)
    return count

my_list=list(map(int,input('Enter List: ').split()))
count_element=int(input('Enter number to calculate repetation: '))

print(f'The element {count_element} is repeated for {count_fun(my_list,count_element)} times.')