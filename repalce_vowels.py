def vowels(inp):
    vowels='AEIOUaeiou'
    for r in inp:
        if r in vowels:
            inp=inp.replace(r,'#')
    return inp

input_string=input('Enter sentence: ')
print(vowels(input_string))