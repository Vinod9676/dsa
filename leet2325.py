key ="the quick brown fox jumps over the lazy dog"
message ="vkbs bs t suepuv"
# ans=""
# s="a"
# key1=""
# for j in key:
#     if j!=" " and j not in key1:
#         key1 +=j
# for k in message:
#     if k != " ":
#         l=key1.index(k)
#         ans +=chr(ord(s)+l)
#     else:
#         ans +=" "
# print(ans)
dict={}
s="a"
c=0
ans=""
for i in key:
    if i not in dict and i !=" ":
        dict[i]=chr(ord(s)+c)
        c +=1
for j in message:
    if j !=" ":
        ans +=dict[j]
    else:
        ans +=" "
print(ans)