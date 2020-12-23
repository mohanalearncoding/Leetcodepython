#nums = [1,2,3,4]
#Output: [1,3,6,10]
from typing import List


def runningSum( nums: List[int]) -> List[int]:
    output=[nums[0]]
    s=nums[0]
    for i in range(1,len(nums)):
        s+=nums[i]
        output.append(s)

    return output
print(runningSum([1,2,3,4]))