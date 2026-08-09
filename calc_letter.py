
string_input=input('Enter Sentence: ').upper()
count=0
for i in (string_input):
    if i.isalpha():
        count+=1

print(count)
