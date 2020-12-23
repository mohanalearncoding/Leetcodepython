from typing import List

#nums = [1,1,1,1]
#Output: 6
def numIdenticalPairs(nums: List[int]) -> int:
       output=0
       i =0
       j=i+1
       while i < len(nums) :
        if j < len(nums):
           if nums[j]==nums[i]  :
               output+=1
               #print(output,i,j)
           j+=1

        else:
            i+=1
            j=i+1
       return output
print(numIdenticalPairs( [1,1,1,1]))