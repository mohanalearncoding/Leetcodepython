from typing import List


def countNegatives( grid: List[List[int]]) -> int:
    c=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]<0:
                c+=1
    return c
print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
