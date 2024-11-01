
nums = [1,2,3,1,1,3]
dict={}
ans=0
for i in nums:
    if i not in dict:
        dict[i]=1
    else:
        dict[i] +=1

for i in dict:
    if dict[i]>1:
        n = dict[i]
        ans += n*(n - 1) / 2
print(chr(ord("a")+1))