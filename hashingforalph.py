sentence=input()
hashtable=[0 for i in range(26)]
for i in sentence:
    hashtable[ord(i)-ord("a")] +=1
q=int(input())
for i in range(q):
    cha=input()
    print(hashtable[ord(cha)-ord("a")])
