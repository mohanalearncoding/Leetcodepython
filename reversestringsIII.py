def reverseWords( s: str) -> str:
    #Input: "Let's take LeetCode contest"
    i=0
    st=""
    temp=""
    l=[]
    #s=s[::-1]
    print(s)
    newstring=""
    for i in range(len(s)):
        if s[i].isspace()==False:
            #print(s[i])
            st+=s[i]
        else:
            #print(st)
            p=st[::-1]
            newstring += p+" "
            print(p)
            st=""
            p=""

    newstring+=st[::-1]       #l.append(p)
    print(newstring)
    #print(st.strip())

    # while i <len(s):
    #     if s[i].isspace()==False :
    #         temp+=s[i]
    #         #print(i,len(s),temp)
    #     else:
    #         l.append(temp[::-1])
    #         temp=""
    #     i+=1
    # l.append(temp[::-1])
    # #print(l)
    # for i in l:
    #     st+=i
    #     st+=" "
    # i=0
    # temp=""
    # while i < len(l):
    #         #print(l[0])
    #         for j in l[i]:
    #             #print(l[j],l[i])
    #             temp=j+temp
    #         st=st+temp+" "
    #         temp=""
    #         i+=1
    # return st.strip(" ")

print(reverseWords( "Let's take LeetCode contest"))