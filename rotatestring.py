def rotateString( A, B):
    if len(A)==0:
        return True
    maxshift=len(A)
    shiftstr=A
    i =0
    while i < maxshift:
        shiftstr=shiftstr[1:]+shiftstr[0]
        if shiftstr==B:
            return True
        else:
            i+=1
        if shiftstr==A:
            return False
print(rotateString( "",""))