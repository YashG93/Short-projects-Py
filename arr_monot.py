
def arr_mono(arr):
    increasing=decreasing=True

    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            decreasing =False
        elif arr[i]<arr[i-1]:
            increasing=False
    
    return increasing or decreasing

arr1=[1,2,3,4]
arr2=[1,2,2,3]
arr3=[1,3,2,4]

print('arr1 is monotonic:',arr_mono(arr1))
print('arr2 is monotonic:',arr_mono(arr2))
print('arr3 is monotonic:',arr_mono(arr3))



