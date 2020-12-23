from itertools import count


def minMoves( nums):
    noofadd=len(nums)-1
    maxelem=max(nums)
    nums=sorted(nums)
    #print(nums.count(nums[0]))
    c=0
    while(nums.count(nums[0])!=len(nums)):
        j=0
        k=0
        for j in range(noofadd):
            nums[k]=nums[k]+1
            k+=1
            print(j,nums)
        c+=1
    return nums
print(minMoves([1,2,3]))