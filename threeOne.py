num=int(input("Enter a number: "))
sum=0
for i in range(1, num-1):
  if(num%i==0):
    sum=sum+i
if(sum==num):
  print("{} is a perfect number".format(num))
else:
  print("{} is not a perfect number".format(num))