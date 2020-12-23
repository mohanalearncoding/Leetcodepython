from collections import Counter
def majorityElement(nums):
#Input: [2,2,1,1,1,2,2,3]
#Output: 2
    d={}
    for i in nums:
      if i in d:
          d[i]=d[i]+1
      else:
          d[i]=1
    print(d)
    m=max(d.values())
    for k,v in d.items():
        if v==m:
            return k

""" c=Counter(nums)
    print(c)
    m=max(c.values())
    for k,v in c.items():
        if v==m:
            return k
"""



print(majorityElement([2,2,1,1,1,2,2,3]))
