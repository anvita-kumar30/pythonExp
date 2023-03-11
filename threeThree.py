def add(*lst):
    sum = 0
    for i in lst:
        sum += i
    print("The sum is: {}".format(sum))
def subtract(*lst):
    res = 0
    for i in lst:
        res -= i
    res += (2*lst[0])
    print("The subtraction is: {}".format(res))
def multiply(*lst):
    multi = 1
    for i in lst:
        multi *= i
    print("The multiplication is: {}".format(multi))

def divide(*lst):
    div = 1
    for i in lst:
        div /= i
    div *= (lst[0]**2)
    print("The division is: {}".format(div))
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
ch = int(input("Choose the operation you wish to perform: "))
n = int(input("Enter the number of operands: "))
lst = []

lst.append([int(x) for x in input("Enter the operands: ").split()])

if(ch == 1):
    add(*lst)
elif(ch == 2):
    subtract(*lst)
elif(ch == 3):
    multiply(*lst)
elif(ch == 4):
    divide(*lst)
else:
    print("Invalid choice")