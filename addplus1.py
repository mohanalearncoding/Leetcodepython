def plusOne( digits):
    as1 = digits[-1] + 1
    # print(as)
    digits.pop()
    if as1<10:
         digits.append(as1)
         return digits
    st=""
    for i in digits:
        st+=str(i)
    s=str(int(st)+1)
    print(s)
    a=[0]*len(s)

    for i in range(len(s)):
        a[i]=s[i]
    return a






    # a=digits[-1]+1
    # print(a)
    # digits.pop()
    # if a<10:
    #     digits.append(a)
    #     return digits
    # else:
    #     temp=str(a)
    #     j=[]
    #     for i in range(len(temp)):
    #         st=int(a%10)
    #         a=a/10
    #         j.append(st)
    #     j=j[::-1]
    #     for i in j:
    #         digits.append(i)
    #     return digits
print(plusOne([9,9]))