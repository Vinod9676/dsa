nums=[1,2,3,4,5,6,7]
# arr1=[]
k=3
# for j in range(len(arr)):
#     i=j-k
#     print(i)
#     if i>=0:
#         b=i%len(arr)
#         arr1.insert(b,arr[j])
#     if i<0:
#         b=len(arr)+i
#         arr1.insert(b,arr[j])
# print(arr1)
# [5,6,7,1,2,3,4]
n=len(nums)
for l in range(k):
    temp=nums[0]
    print(temp)
    for i in range(1,n):
        nums[i-1]=nums[i]

    nums[n-1]=temp
    print(nums)
