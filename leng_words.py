
def len_words(l,length):
    result=[]
    for i in l :
        if len(i)>length:
            result.append(i)

    return result
        
my_list=list(map(str,input('Enter list: ').split()))
leng=3

print(len_words(my_list,leng))