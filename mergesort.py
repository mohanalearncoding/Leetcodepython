def mergeTwoLists( l1, l2):
    if len(l1)==0:
        return l2
    if len(l2)==0:
        return l1
    tot=len(l2)+len(l1)
    arr=[0]*tot
    i,j,k=0,0,0
    while i< len(l1) and j < len(l2):
        if l1[i]<=l2[j]:
            #print(i,j,"1st")
            arr[k]=l1[i]
            i+=1
            #print(arr,i,j,k)
        else:
            #print(i,j)
            arr[k]=l2[j]
            j+=1
            #print(arr, i, j, k,"am")
        #print(i+1,j+1,k,"s")
        k+=1
        if i<k:
            arr[k]=l1[-1]
        if j<k:
            arr[k]=l2[-1]
    return arr
print(mergeTwoLists([], [0]))
