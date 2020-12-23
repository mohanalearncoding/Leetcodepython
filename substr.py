
def strStr( haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    h=len(haystack)
    n=len(needle)
    for i in range(0,h-n+1):
        print(haystack[i:i+n])
        if haystack[i:i+n]==needle:
            #print(haystack[i:h-n+1])
            return i
    return -1



    """if needle[0] in haystack:
        start = haystack.index(needle, 0, len(haystack))
        # print(start)
        i = start
    else:
        # print("hi")
        return -1
    s3 = ""
    j = 0
    # print("ma")

    while j < len(needle):
        if needle[j] == haystack[i]:
            s3 += haystack[i]
            j += 1
            i += 1
        else:
            start = i
            j = 0
            s3 = ""
    if s3 == needle:
        return start
    else:
        return -1
"""
print(strStr("hello","o"))

#print(strStr(s1="hello",s2="ll"))
