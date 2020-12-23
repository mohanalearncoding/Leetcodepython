def reverse( x: int) -> int:

    sx=str(abs(x))
    sx=int(sx[::-1])
    if x<0:
        sx=-sx
    if sx < -2**31 or sx > (2**31)-1:
        return 0
    else:
        return sx

print(reverse(120))