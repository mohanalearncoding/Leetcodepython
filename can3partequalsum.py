def canThreePartsEqualSum(A):
    n=sum(A)//3
    print(n)
    s=0
    c=0
    for i in range(len(A)-1):
        s+=A[i]
        if s==n:
            s=0
            c+=1
            if c==2:
                return True
    return False

print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))