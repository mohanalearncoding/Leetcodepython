from typing import List

#grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
def countNegatives(grid: List[List[int]]) -> int:
   count=0
   for i in grid:
       j=0
       for j in i:
           if j<0:
                count+=1
   return count
print(countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))