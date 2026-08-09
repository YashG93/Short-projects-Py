
def char_str(input_string):
    character = []

    special_chars = '!@#$%^&*()_-+=:;{}[]/<>?.,'

    for i in input_string:
        if i in special_chars:
            character.append(i)

    return character


my_string = input("Enter String: ")
print(f"{char_str(my_string)} are special characters in '{my_string}'")