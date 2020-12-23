def largestSumAfterKNegations( A, K):
    lst=sorted(A)
    c=K
    i=0
    while c>0:
        if lst[i]<=lst[i+1]:
            lst[i]=lst[i] * -1
            c-=1
        else:
            i+=1
    return sum(lst)








    # j=0
    # i =0
    # while j<K:
    #       if A[i]<0 and A[i+1]<0:
    #            A[i]=A[i]*-1
    #
    #            i+=1
    #       elif A[i]>=0:
    #           A[i]=A[i]*-1
    #           print(A)
    #
    #       j+=1

    # for i in range(K):
    #    A[j]=A[j]*(-1)
    #    if A[j]!=0 and A[j+1] <0:
    #        print(A)
    #        j+=1
    return sum(A)
print(largestSumAfterKNegations([1,3,2,6,7,9],3
))