def backspaceCompare( S, T):
    #S = "a#c", T
    # t2="",""
    t1,t2="",""
    for i in S:
        if i=='#':
            t1=t1[0:-2]
        else:
            t1+=i
    for i in T:
        if i=='#':
            t2=t2[0:-1]
            print(t2)
        else:
            t2+=i
            print(t2)


    return (t1==t2)
print(backspaceCompare("xywrrmp","xywrrmu#p"))