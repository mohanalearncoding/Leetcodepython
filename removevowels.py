def removeVowels(S: str) -> str:
#"leetcodeisacommunityforcoders"
    d={'a','e','i','o','u'}
    s=""
    for i in S:
        if i not in d:
            s+=i
    return s
print(removeVowels("leetcodeisacommunityforcoders"))