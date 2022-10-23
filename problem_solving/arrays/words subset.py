
from collections import Counter


def wordSubsets( words1, words2) :
    d = {}
    for w in words2:
        for x in set(list(w)):
            d[x] = max(d.get(x,0),w.count(x))
    ans = []
    for w in words1:
        a = True
        for k,v in d.items():
            if w.count(k)<v:
                a = False
                break
        if a == True:
            ans.append(w)
    return ans

words1=["amazon","apple","facebook","google","leetcode"]
words2=["eo","oo"]
print (wordSubsets(words1,words2))