
def append_lst(lst,num):
    lst.pop(0)
    lst.append(num)
    return lst

input_lst =list(map(int,input('Enter list: ').split(',')))
input_num=int(input('Enter num: '))
print(append_lst(input_lst,input_num))
