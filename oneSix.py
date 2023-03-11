# n=int(input("Enter the range for the pattern: "))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i),end=' ')
#     print()

# for i in range(5,0,-1):
#     print(' '*(5-i) + '*'*i)

row = int(input("Enter how many lines: "))
for i in range(1,row+1):
    for j in range(1, row+1-i):
        print(" ", end="")
        for j in range(1,i+1):
            print(j, end='')
            for j in range(i-1,0,-1):
                print(j, end='')
    print()

