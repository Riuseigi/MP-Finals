def coin(n):
  dic={500:0,200:0,100:0,50:0,20:0,10:0,5:0,1:0}
  while n>0:
        if n>500:
          dic[500]+=1
          n-=500
        elif n>200:
          dic[200]+=1
          n-=200
        elif n>100:
          dic[100]+=1
          n-=100
        elif n>50:
          dic[50]+=1
          n-=50
        elif n>20:
          dic[20]+=1
          n-=20
        elif n>10:
          dic[10]+=1
          n-=10
        elif n>5:
          dic[5]+=1
          n-=5
        elif n>1:
          dic[1]+=1
          n-=1
        else:
          return dic


amnt = int(input("Enter an amount value: "))
total = coin(amnt)
for i in total:
  print(i,'=',total[i])

