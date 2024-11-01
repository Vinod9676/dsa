n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

hashtable=[0 for i in range(10)]

for i in range(n):
    hashtable[arr[i]] +=1

q=int(input())
while q !=0:
    num =int(input())
    q -=1
    print(hashtable[num])
# print(1e7)



