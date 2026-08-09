
def range_divi(x,y,z):
    return[m for m in range(x,y) if m%z==0]

start,end,div=map(int,input('Enter range of numbers: ').split(','))
print(range_divi(start,end,div))
