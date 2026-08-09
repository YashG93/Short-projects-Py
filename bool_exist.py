
def is_bool(n):
    if  isinstance(n,bool):
        return not n
    else:
        return 'boolean expected.'
    
print(is_bool(32))
print(is_bool(True))
print(is_bool('#True'))
print(is_bool(False))
print(is_bool('43f'))