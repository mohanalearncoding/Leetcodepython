from collections import Counter
def numJewelsInStones( J: str, S: str) -> int:
        sum=0
        c=Counter(S)
        for i in J:
            if i in c:
                sum+=c[i]
        return sum
print(numJewelsInStones("z",  "ZZ"))