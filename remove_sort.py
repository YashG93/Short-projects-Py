input_string=input('Enter sentece: ')
new_string=set(input_string.split())

sorted_words=sorted(new_string)

result=' '.join(sorted_words)
print(result)