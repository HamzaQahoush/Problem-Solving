def isIsomorphic( s: str, t: str) -> bool:
    if len(s)!=len(t) or len(set(s))!=len(set(t)):
        return False
    hashmap={}
    
    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]]=t[i]
        
        if hashmap[s[i]]!=t[i]:
            return False
    return True
    
def findAndReplacePattern(words, pattern: str) :
    res=[]
    for word in words:
        check=isIsomorphic(pattern,word)
        if check:
            res.append(word)
    return res



words =["badc","abab","dddd","dede","yyxx"]

pattern = "baba"

print(findAndReplacePattern(words,pattern))


