from functools import lru_cache


@lru_cache(maxsize=None)
def climbStairs( n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)
print(climbStairs(38))