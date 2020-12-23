def isHappy( n):
    def get_next(n):
        sum=0
        while n>0:
            n,digit=divmod(n,10)
            print(digit)
            sum=sum+(digit ** 2)
        return sum
    s=set()
    while n!=1 and n not in s:
        s.add(n)
        n=get_next(n)

    return n==1
print(isHappy(19))