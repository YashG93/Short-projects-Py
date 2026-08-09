
X,Y=map(int,input('Enter two digits (X,Y): ').split(','))

array=[[0 for i in range(Y)] for i in range(X)]

for i in range(X):
    for j in range(Y):
        array[i][j]=i*j

for row in array:
    print(row)





