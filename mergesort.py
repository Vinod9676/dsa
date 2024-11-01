def merge(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge(left)
    merge(right)
    return ms(left,right)
def ms(left,right):
    sorted_list=[]
    a=len(left)
    b=len(right)
    i=0
    j=0
    while i<a and j<b:
        if left[i]<=right[j]:
            sorted_list.append(left[i])
            i +=1
        elif right[j]<=left[i]:
            sorted_list.append(right[j])
            j +=1
    while i<a:
        sorted_list.append(left[i])
        i +=1
    while j<b:
        sorted_list.append(right[j])
        j +=1
    return sorted_list
arr=[1,2,4,4,1,2,5,6]
print(merge(arr))