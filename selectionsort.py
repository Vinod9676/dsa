arr=[13,46,24,52,20,9]
for i in range(len(arr)-1):
    min=i
    for j in range(i,len(arr)):
        if(arr[j]<arr[min]):
            min=j
    temp=arr[min]
    arr[min]=arr[i]
    arr[i]=temp
print(arr)