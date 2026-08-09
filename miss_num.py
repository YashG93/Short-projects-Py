
def missing_num(lst):
    total=sum(range(1,11))
    lst_sum=sum(lst)
    miss_num=total-lst_sum
    return miss_num

input_list=list(map(int,input('Enter number list: ').split(',')))
print(missing_num(input_list))
print(sum(input_list))

