from collections import Counter
def isAnagram(s, t):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    for i in t:
        if i in d:
            d[i]-=1
        else:
            return False
    print(ord('A'),ord('C'))
    for v in d.values():
        if v!=0:
            print(v)
            return False
    return True
    # cs=Counter(s)
    # ct=Counter(t)
    # flag=True
    # print(ct,cs)
    # if len(s)!=len(t):
    #      return False
    #
    # for i in t:
    #     if i in s:
    #         print(i)
    #         if ct[i]==cs[i]:
    #             flag=True
    #
    #         else:
    #             flag=False
    #     else:
    #         return False
    # return flag
print(isAnagram("anagram",
"nagaram"))