import math
def maximumProduct( nums):
    #[-1,-2,-3,1]
    nums.sort()
    return max((nums[0]*nums[1]*nums[-1]),(nums[-1]*nums[-2]*nums[-3]))
print(maximumProduct( [-100,-98,-1,2,3,4]))