from typing import List


def kidsWithCandies( candies: List[int], extraCandies: int) -> List[bool]:
# candies = [2, 3, 5, 1, 3], extraCandies = 3
       op=[]
       maxi=max(candies)
       for i in candies:
           if i+extraCandies >=maxi:
               op.append(True)
           else:
               op.append(False)
       return op












       """ maxcandy=max(candies)
        output=[]
        for i in candies:
            if extraCandies+i >=maxcandy:
                output.append('true')
            else:
                output.append('false')
        return output"""
print(kidsWithCandies([2, 3, 5, 1, 3],  3))
