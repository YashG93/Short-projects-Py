numb=[54,23,62,35,74,24,19]
temp=1
k=0
for i in numb:
    if i>temp:
        temp=i
        if i==temp:
            pass
        elif i>k :
            k=i

k=0

for i in numb:
    if i==temp:
        pass
    
    elif i>k :
        k=i


print(k)

    