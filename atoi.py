def myAtoi( s: str) -> int:
    l = len(s)
    i = 0
    num = 0
    s=s.lstrip()
    print(s)
    if s[i]=='-':
        mul=-1
        i=1
    elif s[i]=='+':
        mul=1
        i=1
    else:
        mul=1
    startpoint=i
    if len(s)==0:return 0

    while i<len(s) and s[i].isdigit():
        i+=1
        
    str=s[startpoint:i]
    print(str)
    if str:
        str=int(str)
    else:
        return 0
    str=str*mul
    if str>2**31 - 1:
        str=2**31
    if str<-2**31:
        str=-2**31
    return str
print(myAtoi("  -42"))