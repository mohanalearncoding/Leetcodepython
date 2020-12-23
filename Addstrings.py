def addStrings(num1, num2):
    d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    s1,s2=0,0
    num1=num1[::-1]
    num2=num2[::-1]
    for i in range(len(num1)):
        s1+=(10 ** i)*d[num1[i]]
    for i in range(len(num2)):
        s2+=(10 ** i)*d[num2[i]]
    s1= s1+s2
        
print(addStrings('2','20'))