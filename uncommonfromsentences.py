from typing import List
from collections import Counter

def uncommonFromSentences(A: str, B: str) -> List[str]:
    a =[]
    b=[]
    st=""
    def char2str(C:str,x)->List[str]:
        st = ""
        for i in C:
            st=st+i

            if i.isspace():
                st=st.strip()
                x.append(st)
                st=""
        x.append(st)
    char2str(A,a)
    char2str(B,b)
    print(a,b)
    arr=[]
    ca=Counter(a)
    cb=Counter(b)
    print(ca,cb)

    for i in a:
        if i not in b and ca[i]==1:
            arr.append(i)
    for i in b:
        if i not in a and cb[i]==1:
            arr.append(i)
    return arr
print(uncommonFromSentences("this apple is sweet", "this apple is sour"))