def merge( nums1, m, nums2, n):
    nums=nums1[:m]
    nums1[:]=[]
    print(nums,nums1)
    c1=0
    c2=0
    while c1<m and c2<n:
        if nums[c1]<nums2[c2]:
            nums1.append(nums[c1])
            c1+=1
        else:
            nums1.append(nums2[c2])
            c2+=1
    if c1<m:
        nums1[c1+c2:]=nums[c1:]
    if c2<n:
        nums1[c1+c2:]=nums2[c2:]

    return nums1










print(merge(nums1 = [1,2,3,0,0,0,0], m = 3,nums2 = [2,5,6],       n = 4))
# def binarysearch(nums1,k):
    #     mid=len(nums1)//2
    #     print("mid",mid,nums1[mid])
    #     if nums1[mid]<=k:
    #         print("here")
    #         nums1.insert(mid+1,k)
    #         return nums1
    #         print(nums1,"l")
    #
    #     else:
    #         binarysearch(nums1[:mid],k)
    #
    #
    # for i in range(len(nums2)):
    #      if nums2[i]>=nums1[m-1]:
    #          nums1.insert(m,nums2[i])
    #      elif nums2[i]<nums1[m-1]:
    #         print("am")
    #         nums1=binarysearch(nums1[:m],nums2[i])
    #         print(nums1)
    #      m+=1
    # return nums1