def reverse_between_bracket(s):
    stack=[]
    
    for ch in s :
        if ch == ")":
            tmp=""
            while stack[-1] != "(":
                tmp+=stack[-1]
                stack.pop()
            stack.pop()
            for t in tmp:
                stack.append(t)
                
        else:
            stack.append(ch)
    return "".join(stack)
       
s="(abc)d(efg)"
print(reverse_between_bracket(s))