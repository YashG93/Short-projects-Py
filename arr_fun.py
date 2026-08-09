

def arr_rec():
        m=0
        for n in arr:
            m+=n
        return m

arr=list(map(int,input('Enter arr: ').split()))
print(arr_rec())



