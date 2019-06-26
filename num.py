      ld1=int(input())
    n1=list(map(int,input().split()))
   tj=[]
     for x in range(ld1):
         for i in range(x+1,len(n1)):
           if(n1[i]==n1[x]):
            tj.append(n1[x])

    if (len(tj)==0):
         print("unique")
   else:
       print(tj[0])
