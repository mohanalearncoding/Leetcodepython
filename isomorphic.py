from collections import Counter
from itertools import count


def isIsomorphic( s, t):
    d={}
    for i in range(len(s)):

        if s[i] in d:
            if d[s[i]]!=t[i]:
                return False

        else:
            d[s[i]]=t[i]
            print(d)
    vals=Counter(d.values())
    print("v",vals)
    for k,v in d.items():
        if vals[v]>1:
            return False

    return True
print(isIsomorphic("egg",
"add"))