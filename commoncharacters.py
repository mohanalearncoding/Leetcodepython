from collections import Counter
def commonChars(A):
    result=[]
    A.sort(key=lambda x: len(A))
    shortest=Counter(A[0])
    for i in A[1:]:
        for j in shortest:
            shortest[j]=min(shortest[j],i.count(j))
    for k,v in shortest.items():
        if v>=1:
            for _ in range(v):
                result.append(k)
    return result
print(commonChars(["bella","label","roller"]))