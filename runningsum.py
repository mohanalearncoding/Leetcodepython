from typing import List


def runningSum( nums: List[int]) -> List[int]:
    #[1, 2, 3, 4]
    op=[nums[0]]
    sum=nums[0]
    for i in range(1,len(nums)):
        sum+=nums[i]
        op.append(sum)
    return op
print(runningSum([3]))
