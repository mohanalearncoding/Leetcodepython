def findsum(str1):
    s='0'
    total=0
    for i in str1:
        #print(i)
        if i.isdigit():
            s+=i
        else:

            total+=int(s)
            print(total)
            s='0'
    total+=int(s)
    return total
print(findsum('afiefiyh485rgfvrkjiv85rgrm'))
