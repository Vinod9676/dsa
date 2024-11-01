arr=[13,46,24,52,20,9]
for i in range(1,len(arr)):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        temp =arr[j]
        arr[j]=arr[j-1]
        arr[j-1]=temp
        j -=1
print(arr) 