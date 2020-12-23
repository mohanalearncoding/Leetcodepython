def findLengthOfLCIS( nums):
    c=1
    maxi=1
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            c+=1
            print(c)

        else:
            c = 1
        maxi = max(maxi, c)


    return maxi
print(findLengthOfLCIS([1,3,5,4,2,3,4,5]))