for n in range(1,1000):
    sum=0
    temp=n
    while temp>0:
        num=temp%10 
        sum=sum+num**3
        temp//=10
        if n==sum:
            print(n)
