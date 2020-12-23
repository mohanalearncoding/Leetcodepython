def findJudge( N, trust):
    d={}
    arr=[[1,2]]*len(trust)
    print(arr)
    if N==1:
        return 1
    for i in range(len(trust)):
        if trust[i][1] not in d:
            d[trust[i][1]]=1
        else:
            d[trust[i][1]]+=1
    for i in range(len(trust)):
        if trust[i][0] in d:
            d[trust[i][0]]-=1
    print(d)
    for k,v in d.items():
        if v==(N-1):
            return k
    return -1
print(findJudge(2,[]))
