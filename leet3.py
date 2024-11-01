s =" "
k = ""
c = 0
ans = 0
for i in s:
    if i not in k:
        k += i
        c += 1
    else:
        k = ""
        k += i
        ans = max(ans, c)
        c = 1
ans=max(ans,c)
print(ans)