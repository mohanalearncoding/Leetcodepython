import operator
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:

   #logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
   numarr=[]
   alparr=[]
   result=[]
   st=[]
   d={}
   s=""
   for i in logs:
        sep=i.split(" ",1)
        print(sep)
        if sep[1][0].isdigit():
            numarr.append(i)
        if sep[1][0].isalpha():
            alparr.append(i)
            #st.append(sep[1])
            #d[sep[0]]=sep[1]
   # print(st)
   # st.sort()#(key=lambda x:x[0])
   # print(st,d,"sor")
   # for i in st:
   #     for k,v in d:
   #         if v==i:
   #             return k
   #     s=k+" "+i
   #     alparr.append(s)
   alparr.sort(key=lambda x: (x.split()[1:],x.split()[1]))
   print(alparr)
   result=alparr+numarr

   print(result,alparr,numarr)
   return result
print(reorderLogFiles( ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
#["t kvr","7 so","r 3 1","i 403","t 54"]


#
# #       if i[5].isalpha():
#            alparr.append(i)
#        if i[5].isdigit():
#            numarr.append(i)





















   # for _ in logs:
   #      split_it = _.split(" ")
   #      if split_it[1].isdigit():
   #          numarr.append((" ".join(split_it[:])))
   #          #print(numarr)
   #      else:
   #          alparr.append([split_it[0]," ".join(split_it[1:])])
   #          print(alparr)
   # #print(alparr,numarr)
   # for i in sorted(alparr,key=operator.itemgetter(1,0)):
   #     result.append(" ".join(i))
   # #result+numarr
   # return result+numarr
   #
   # #logs=sort(alparr,key=)+numarr
   # #return logs
   #

#print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))