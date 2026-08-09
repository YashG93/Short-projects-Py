
def check_fun(string1,string2):
    count=0
    for n in range(1,len(string2)):
        if string1[n]==string2[n]:
            count+=1
    return count

first_string=input('Enter word: ')
second_string=input('Enter word: ')
print(f'{check_fun(first_string,second_string)} letter is same.')


