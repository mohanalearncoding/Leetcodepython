def arrayRankTransform( arr):
    arr1=sorted(arr)
    print(arr1)
    retarr=[None]*len(arr)
    d={}
    rank=1
    for i in arr1:
        if i not in d:
            d[i]=rank
            rank+=1

    for idx,i in enumerate(arr):
        arr[idx]=d[i]
    return arr





print(arrayRankTransform([100,100,100]))