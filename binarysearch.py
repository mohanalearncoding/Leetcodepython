def search(nums, target):

    def recursearch(right,left,target,nums):
        if left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return recursearch(right,mid+1,target,nums)
            elif nums[mid]>target:
                return recursearch(left,mid-1,target,nums)
            else:
                return -1

    right, left = 0, len(nums) - 1
    return recursearch(right,left,target,nums)
print(search([-1,0,3,5,9,12], 9))