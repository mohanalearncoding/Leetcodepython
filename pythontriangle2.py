def getRow(rowIndex):
        rowIndex=rowIndex+1
        arr=[[0]]*rowIndex
        if rowIndex==0:
            return []
        if rowIndex==1:
            return [1]
        arr[0] = [1]
        arr[1] = [1, 1]
    #print(arr)
        for i in range(2,rowIndex):
            arr[i]=[0]*(i+1)
            print(arr)
            arr[i][0]=1
            arr[i][-1]=1
            for j in range(1,len(arr[i])-1):
                arr[i][j]=arr[i-1][j]+arr[i-1][j-1]

        return arr[rowIndex-1]
    #print(a)

print(getRow(3))
