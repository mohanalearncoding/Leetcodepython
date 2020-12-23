from collections import Counter
from typing import List


def mostCommonWord( paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()
    stri=""
    for c in paragraph:
        if c.isalnum():
          stri+=c
        else:
            stri=stri+(" ")
    words=stri.split()
    c=Counter(words)
    print(stri,words,c)
    counter=0
    stri=""
    for i in words:
        if i not in banned:
           if c[i]>counter:
               counter=c[i]
               stri=i
    return stri
print(mostCommonWord("Bob","[]"))




"""paragraph = "Bob. hIt, baLl"

paragraph=paragraph.lower()
print("para",paragraph)
banned=["bob", "hit"]
i=0
p=[]
s=""
if len(banned)<1:
    print(paragraph.strip("!?',;."))
while i<len(paragraph):

    if paragraph[i].isspace()==False and paragraph[i] not in ("!?',;.") and i !=len(paragraph)-1:
        s+=paragraph[i]
        print(s,i,len(paragraph))
        i+=1
    else:
        print(s,"insideelse")
        if s not in banned:
                print(s,"ss")
                p.append(s)
                print(p,len(p))
        s = ""
        i+=1
words=
print(words,"w")
c=Counter(p)
currmax=0
s1=""
for i in p:
        print(i,c,"chk")
        if currmax<c[i]:
            currmax=c[i]
            s1=i
#print(c)
"""