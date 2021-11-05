N=int(input("Please enter a number:"))
sum0 = 0
sum1= 0
x=0
for i in range (1,N+1):
     if i%2==0:
        sum0= sum0+i
        x+=1
     else:
        sum1 = sum1 + i
print("average of even nums=",(sum0/x))
print("sum of odd nums=",sum1)