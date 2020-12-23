from typing import List


def checkPossibility(nums: List[int]) -> bool:
    i=1
    while i< len(nums):
        if nums[i-1]<nums[i]:
            if all(nums[j] < nums[j + 1] for j in range(i, len(nums) - i)):
                i+=1
                print("a,")
            else:
                print("k")
                return False
        else:
                nums[i-1]=nums[i]-1
                print(nums,i)
                if all(nums[j]<nums[j+1] for j in range(i,len(nums)-i)):
                    return True
                else:
                    return False

print(checkPossibility( [-1,4,2,3]
))


