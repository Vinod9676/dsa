import math

n = 11010
# l=n
# ans=0
# mul=1
# for i in range(len(l)):
#     if l[i]=="1":
#         ans +=mul
#     mul *=2
# print(ans)
result = 0
for i in range(32):
    # result = (result << 1) | (n & 1)
    result = (n & 1)
    print(result)
    n >>= 1