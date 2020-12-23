from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    #Input: nums = [1, 2, 3, 1, 1, 3]
    #Output: 4
    #(0,3), (0,4), (3,4), (2,5)
    output=0
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] == nums[j]):
                    output += 1
    return output
print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))