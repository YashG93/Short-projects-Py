
def dupli_char(input_string):
    duplicate=[]
    seen=[]

    for i in input_string:
        if i in seen:
            if i not in duplicate:
                duplicate+=i

        else:
            seen.append(i)

    return duplicate
my_string=list(map(str,input('Enter String: ')))
print(f'{dupli_char(my_string)}')










