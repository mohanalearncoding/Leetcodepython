from typing import List


def sortArrayByParityII( A: List[int]) -> List[int]:
    #[4,2,5,7]
    """ dodd=[]
    deven=[]
    arr=[]
    j=k=0
    for i in A:
        if i%2==0:
            deven.append(i)
        else:
            dodd.append(i)
    for i in range(len(A)):
        if i%2==0:
            arr.append(deven[j])
            j+=1
        else:
            arr.append(dodd[k])
            k+=1
    """
    ec=0
    odd=1
    arr=[0]*len(A)
    for i in A:
        if i%2==0:
            arr[ec]=i
            ec+=2
        else:
            arr[odd]=i
            odd+=2


    return arr
print(sortArrayByParityII([4,2,5,7]))