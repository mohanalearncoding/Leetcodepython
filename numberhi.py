# Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
# countHi("xxhixx") → 1
# countHi("xhixhix") → 2
# countHi("hi") → 1
def countHi(s:str)->int:
    if len(s)<=1:
        return 0

    if s[0:2]=='hi':
        return 1 + countHi(s[2:])
    return countHi(s[1:])
print(countHi("xhixhix"))
