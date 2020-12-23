def countAndSay( n):



        val=""
        res='1'
        for i in range(n-1):
            cnt=1
            for j in range(len(res)-1):
                if res[j]==res[j+1]:
                    cnt+=1
                else:
                    val+=str(cnt)+res[j]
                    cnt=1
            val+=str(cnt)+str(res[-1])
            res=val
            val=""
        return res

print(countAndSay(4))
