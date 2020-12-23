from collections import Counter
def canConstruct(ransomNote, magazine):
    c=Counter(ransomNote)
    print(c)
    flag=True
    for i in magazine:
        if i in c:
            c[i]-=1
            if c[i]<0:
                c[i]=0
    for v in c.values():
        if v==0:
            flag=True
        else:
            return False
    return flag
print(canConstruct("bg",
"efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))