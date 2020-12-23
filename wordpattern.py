from collections import Counter


def wordPattern( pattern, s:str):
    s=s.split()
    seenvalues=[]
    d={}
    st=0
    if len(pattern)!=len(s):
        return False
    for i in pattern:

        if i not in d:
            if s[st] in seenvalues:
                return False
            else:
                d[i]=s[st]
                seenvalues.append(s[st])
        else:
            if d[i]!=s[st]:
                return False
        st+=1
        print(d,seenvalues)
    return True



print(wordPattern(pattern ="aaa",s="aa aa aa aa"))
#
# p=0
#     for i in pattern:
#         if i in d:
#             if d[i]==l[p]:
#                 d.pop(i)
#             else:
#                 return False
#
#         else:
#             d[i]=l[p]
#         p+=1
#         print(d)
#     return len(d)==0