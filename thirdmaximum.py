from typing import List


def thirdMax(nums: List[int]) -> int:

    nums=set(nums)
    #print(nums)
    imax=max(nums)
    if len(nums)<3:
        return imax
    max3=0
    for i in range(3):
        max3=max(nums)
        nums.remove(max3)
    return max3
print(thirdMax( [12, 3, 8, 9, 12, 12, 7, 8, 12, 4, 3, 8, 1]))