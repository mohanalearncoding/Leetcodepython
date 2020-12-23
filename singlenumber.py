from typing import List
from collections import Counter

def singleNumber(nums: List[int]) -> int:
    """c=Counter(nums)
    for k,v in c.items():
        if v==1:
            return k
"""
    nums=sorted(nums)
    #print(nums)

    i =1
    while i < len(nums):
        #print(nums[i])
        if nums[i]!=nums[i-1]:
            return nums[i-1]
        else:
            i+=2
    return nums[-1]


print(singleNumber([4,1,2,1,2]))
