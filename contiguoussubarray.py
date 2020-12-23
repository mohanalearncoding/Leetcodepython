def findMaxAverage( nums, k):
    maximumsum=0
    j=0
    for i in range(k,len(nums)):
           s=sum(nums[j:i])
           maximumsum=max(s,maximumsum)
           j+=1
    return maximumsum/k

print(findMaxAverage([1,12,-5,-6,50,3], k = 4))