
n = 4
k = 11
v="0"
for  i in range(n-1):
    p="1"
    g=""
    for j in range(len(v)-1,-1,-1):
        if v[j]=="0":
            g +="1"
        elif v[j]=="1":
            g +="0"

    v +=p
    v +=g
    print(v)
print(v[4])

S2 = "011"
S3 = "0111001"
S4 = "011100110110001"