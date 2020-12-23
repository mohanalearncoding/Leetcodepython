def findDisappearedNumbers( nums):
    nums=set(nums)
    print(nums)
    a =[]
    m=max(nums)
    if len(nums)==0:
        return a
    for i in range(0,m):
        if i+1 not in nums:
            a.append(i+1)
    return a
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))