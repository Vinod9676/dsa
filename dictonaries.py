n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
dict ={}
for i in range(n):
    dict[arr[i]] =0
for i in range(n):
    dict[arr[i]] +=1
q=int(input())
for i in range(q):
    num =int(input())
    print(dict[num])
