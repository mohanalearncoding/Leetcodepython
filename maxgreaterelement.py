from typing import List


def nextGreaterElement( nums1: List[int], nums2: List[int]) -> List[int]:
    arr=[]
    d={}
    for i,pos in enumerate(nums2):
        d[pos]=i

    for j in nums1:
        position=d[j]
        if position !=len(nums2)-1:
            for i in range(position,len(nums2)):
                if nums2[i]>j:
                    arr.append(nums2[i])
                    break
                if i+1==len(nums2):
                    arr.append(-1)
                    break
        else:
            arr.append(-1)
    return arr
print(nextGreaterElement([2,4],[1,2,3,4]))