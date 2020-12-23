class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        arr=[None]*len(nums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        for k in range(len(self.nums)):
            self.arr[k+1]=sum(self.nums[i:j])
        return self.arr[k+1]
    print(numArray.sumRange(0, 2))