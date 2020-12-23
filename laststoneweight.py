from typing import List


def lastStoneWeight(stones: List[int]) -> int:
#Input: [2, 7, 4, 1, 8, 1]
#Output: 1
    #stones=sorted(stones)
    #print(stones)
    for i in range(len(stones)):
        stones = sorted(stones)
        print(stones[-1],stones[-2])
        if len(stones)==1:
            return stones[0]
        if stones[-1]==stones[-2]:
            stones.pop()
            stones.pop()
            if len(stones)==0:
                return 0
        elif stones[-1]>stones[-2]:
            temp=stones[-1]-stones[-2]
            stones.pop()
            stones[-1]=temp
            print(stones)
    return 0




print(lastStoneWeight([2,2]))
