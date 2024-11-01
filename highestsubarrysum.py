k=[5,9,1,8,7]
n=3
max=0
for i in range(len(k)-n+1):
    val=0
    for j in range(i,i+n):
        val +=k[j]
    if val>max:
        max=val
print(max)

