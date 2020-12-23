def isPalindrome( s:str):
    s=s.lower()
    st=""
    for i in s:
        if i.isalnum():
            st+=i
    print(st,st[::-1])
    return st==st[::-1]
print(isPalindrome("race a car"))