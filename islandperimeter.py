from typing import List


def islandPerimeter( grid: List[List[int]]) -> int:
    totalperimeters=0
    connections=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                totalperimeters+=4
                print(totalperimeters)
                if i!=0 and grid[i-1][j]==1:
                    connections+=1
                    print(connections,"1")
                if j!=0 and grid[i][j-1]==1:
                    connections+=1
                    print(connections,"2")
    return totalperimeters-(connections*2)
print(islandPerimeter( [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))