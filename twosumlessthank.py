from typing import List

#nums = [34,23,1,24,75,33,54,8], k = 60
def twoSumLessThanK( nums: List[int], k: int) -> int:

    nums=sorted(nums)
    #print(nums)
    rightpointer=len(nums)-1
    leftpointer=0
    result=-1
    while leftpointer<rightpointer:
        val=nums[rightpointer]+nums[leftpointer]
        if val<k:
            result=max(result,val)
            leftpointer+=1
        else:
            rightpointer-=1
    return result


print(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))