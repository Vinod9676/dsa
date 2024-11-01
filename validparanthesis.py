s ="){"
if len(s)%2 !=0:
    print("false")
stack=["0"]
for i in s:
    print(i)
    if i=="(":
        stack.append(i)
    elif i=="[":
        stack.append(i)
    elif i=="{":
        stack.append(i)
    elif i==")":
        if stack[-1]=="(":
            stack.pop()
        else:
            stack.append(i)
            break
    elif i=="]":
        if stack[-1]=="[":
            stack.pop()
        else:
            stack.append(i)
            break
    elif i=="}":
        if stack[-1]=="{":
            stack.pop()
        else:
            stack.append(i)
            break
stack.pop()
if len(stack)==0:
    print("True")
else:
    print("false")