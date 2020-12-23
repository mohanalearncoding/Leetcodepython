from typing import List

#arr = [17,18,5,4,6,1]
def replaceElements( arr: List[int]) -> List[int]:
    a = arr[::-1]
    print(a)
    for i in range(len(arr)-1):
        arr[i]=max(arr[(i+1):len(arr)])
    arr[-1]=-1
    return arr
print(replaceElements(arr = [17,18,5,4,6,1]))