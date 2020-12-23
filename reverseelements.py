def removeElement(nums, val):
    count=0
    for i in range(len(nums)):
        if nums[i]==val:
            count+=1
            nums[i]=-1
    return len(nums)-count
print(removeElement([3,2,2,3],
3))