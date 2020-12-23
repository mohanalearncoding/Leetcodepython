#releaseTimes = [9,29,49,50], keysPressed = "cbcd"
def slowestKey(releaseTimes, keysPressed):
    key=keysPressed[0]
    maxi=releaseTimes[0]
    diff=0
    prev=0
    for i in range(1,len(keysPressed)):
        diff=releaseTimes[i]-releaseTimes[i-1]
        if diff>maxi:
            maxi=diff
            key=keysPressed[i]
        elif diff==maxi:
            key=max(keysPressed[i],key)
    return key
print(slowestKey([1,2],"ba"))
"""
        #print(maxi,"maxi")
        if diff not in d:
            d[diff]=keysPressed[i]
            print(d)
        else:

            if str(d[maxi])< str(keysPressed[i]):
                d[maxi]=keysPressed[i]
        print(d)
    print('c'>'b')
    return d[maxi]"""
