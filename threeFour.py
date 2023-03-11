def fact(n):
  if(n==1):
    return n
  else:
    return n*fact(n-1)
number=int(input("Enter a number: "))
if(number<0):
  print("Factorial does not exist")
else:
  print("Factorial of",number,"is ",fact(number))