A=set()
B=set()
print("Enter set A: ")
n = int(input("Enter number of elements: "))
for i in range(0,n):
    ele = input()
    A.add(ele)
print("Enter set B: ")
n = int(input("Enter number of elements: "))
for i in range(0,n):
    ele = input()
    B.add(ele)
choice = 0
while(choice!=5):
    choice = int(input("\n1.Display\n2.Intersection\n3.Union\n4.A-B\n5.End\nEnter your choice: "))
    if(choice==1):
        print("Set A is")
        print(A)
        print("Set B is")
        print(B)
    if (choice == 2):
        print("A intersection B is")
        I = A.intersection(B)
        print(I)
    if (choice == 3):
        print("A union B is")
        U = A.union(B)
        print(U)
    if (choice == 4):
        print("A-B is")
        C = A.difference(B)
        print(C)

