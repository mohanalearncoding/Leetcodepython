def findMaxConsecutiveOnes( nums):
    maxcount=0
    count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        if nums[i]==0 or i==len(nums)-1:
            maxcount=max(maxcount,count)
            count=0
    return maxcount
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))