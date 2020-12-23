from typing import List


def calPoints( ops: List[str]) -> int:
    arr=[]
    s1=0

    for i in range(len(ops)):
        if ops[i]=='C':
            arr.pop()
        elif ops[i]=='D':
            s1=int(arr[-1])*2
            #print(s1,"s1")
            arr.append(s1)
        elif ops[i]=='+':
            s1=int(arr[-1])+int(arr[-2])
            arr.append(s1)
        else:
            arr.append(int(ops[i]))
            #print(arr)
    return sum(arr)
print(calPoints(["1"]))