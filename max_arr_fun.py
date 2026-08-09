
def max_arr():
    j=arr[0]
    for i in arr:
        if i>j:
            j=i
    return j

arr=list(map(int,input('Enter array: ').split()))
print(f"Maximum number in array is {max_arr()}")

