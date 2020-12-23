from typing import List


def intersection( nums1: List[int], nums2: List[int]) -> List[int]:
    nums1=set(nums1)
    nums2=set(nums2)
    arr=[]
    for i in nums1:
        if i in nums2:
            arr.append(i)

    return arr
print(intersection([1,2,2,1],[2,2]))
