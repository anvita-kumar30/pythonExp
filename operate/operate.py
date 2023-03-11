def add(*lst):
    sum = 0
    for i in lst:
        sum += i
    print("The sum is: {}".format(sum))

def multiply(*lst):
    multi = 1
    for i in lst:
        multi *= i
    print("The multiplication is: {}".format(multi))

def evensum(*lst):
    sum = 0
    for i in range(len(lst)):
        if(i%2 == 0):
            sum += lst[i]
    print("Sum of elements at even indices is: {}".format(sum))

def addlist(*lst):
    lst3 = []
    for i in lst:
        lst3.append(i)
    n = int(input("Number of elements you want to append: "))
    print("Enter the elements:")
    lst3.append([int(x) for x in input("Enter the operands: ").split()] )
    print("The list is:")
    for i in range(len(lst3)):
        print(lst3[i], end = " ")
print()