def longestCommonPrefix( strs):
    if len(strs)==0:
        return ""
    if len(strs)==1:
        return strs[0]

    #print(s)
    pattern=""
    
    for i in range(len(min(strs))):
            s=strs[0][i]
            if all(c[i]==s for c in strs):
                pattern+=s
            else:
                break
    return pattern

    #print(count,pattern)
print(longestCommonPrefix(["flower","flow","flight"
]))