

def div(l,m,n):
    result=[]
    for o in range(l,m+1):
        if o%n==0:
            result.append(o)
    return sum(result)
    
g,h,i=map(int,input('Enter number separated by ",":  ').split(','))
print(div(g,h,i))




