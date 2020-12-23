from collections import Counter
def firstUniqChar(s: str) -> int:
    """d={}
    pos=0
    curr=1
    for i in range(len(s)+1):
        if s[i] not in d:
            d[s[i]]=i
            pos=i
            print(d)
        else:
            d[s[i]]=-1


    print(min(d.values()))
"""
    c=Counter(s)
    #print(c)
    for i in range(len(s)):
        if c[s[i]]==1:
            return i

print(firstUniqChar("loveleetcode"))