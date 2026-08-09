
num=int(input('Disarium numbers upto: '))

for i in range(0,num+1):
    for j in range(0,10):
        if i+(j**2)==int(str(i)+str(j)):
            print (f'{i},{j} is disarium numbers.')

