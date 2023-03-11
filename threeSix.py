import operate as op
print("1. Summation of all elements")
print("2. Product of all elements")
print("3. Summation of elements at even indices")
print("4. Add elements in the list")
ch = int(input("Choose the operation you wish to perform: "))
n = int(input("Enter the number of operands: "))
lst = []
lst = [int(x) for x in input("Enter the operands: ").split()]
if(ch == 1):
    op.add(*lst)
elif(ch == 2):
    op.multiply(*lst)
elif(ch == 3):
    op.evensum(*lst)
elif(ch == 4):
    op.addlist(*lst)
else:
    print("Invalid choice")