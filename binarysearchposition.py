from typing import List


def search( nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        def helper(nums,right,left,target):
            mid=(right+left)//2
            #print(mid)
            if left>=right:
                return -1
            if nums[mid]==target:
                return mid+left+right
            if  nums[mid]<target:
                #print("amhere",nums[mid+1:],len(nums)-1,mid)
                return helper(nums[mid:],len(nums)-1,mid,target)
            else:
                return helper(nums[0:mid],mid,0,target)

        return helper(nums,right,left,target)
print(search( nums =  [-1,0,3,5,9,12], target = 2))
