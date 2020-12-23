def mySqrt( x):
    half=x//2
    while True:
        if half*half==x:
            return half
        else:
            half=half//2
            if half*half<=x:
                break
    while True:
        sqr=half*half
        if sqr>x:
            half=half-1
            break
        else:
            half=half+1
    return half
a =4

print(mySqrt(5286943))