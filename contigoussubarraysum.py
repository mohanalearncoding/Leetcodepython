def maxSubArray(nums):
    maxsumsofar=nums[0]
    maxendinghere=nums[0]
    sum=0
    if len(nums)==1:
        return nums[0]
    for i in range(1,len(nums)):

        if maxsumsofar<0:
            maxsumsofar=nums[i]
        else:
            maxsumsofar += nums[i]
            print("m", maxsumsofar)

        maxendinghere=max(maxsumsofar,maxendinghere)
    return maxendinghere
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
