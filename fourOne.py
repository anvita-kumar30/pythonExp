while True:
    print("1. Put even and odd elements in two different lists")
    print("2. Merge and sort two lists")
    print("3. Update the first element with a value X to the list")
    print("4. Print middle element of the list")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if(choice==1):
        def splitevenodd(A):
            evenlist = []
            oddlist = []
            for i in A:
                if(i%2==0):
                    evenlist.append(i)
                else:
                    oddlist.append(i)
            print("Even List:",evenlist)
            print("Odd List:",oddlist)
        A=list()
        n=int(input("Enter the size of the list::"))
        print("Enter the element of the list::")
        for i in range(int(n)):
            k = int(input(""))
            A.append(k)
            splitevenodd(A)
    elif(choice==2):
        a = []
        c = []
        n1 = int(input("Enter number of elements for first list:"))
        print("Enter elements")
        for i in range(1,n1+1):
            b=int(input(""))
            a.append(b)
        n2 = int(input("Enter number of elements for second list:"))
        print("Enter elements")
        for i in range(1,n2+1):
            d=int(input(""))
            c.append(d)
        new = a+c
        new.sort()
        print("Sorted list is:",new)
    elif(choice==3):
        a = []
        n1 = int(input("Enter number of elements:"))
        print("Enter elements")
        for i in range(1, n1 + 1):
            b = int(input(""))
            a.append(b)
        print(a)
        c = int(input("Enter the element:"))
        a[0] = c
        print("Updated list is:",a)
    elif(choice==4):
        a = []
        n1 = int(input("Enter number of elements:"))
        print("Enter elements")
        for i in range(1, n1 + 1):
            b = int(input(""))
            a.append(b)
        n = round(n1/n2)
        print("Middle element =",a[n])
    else:
        print("Invalid Choice")
        repeat = input("Do you want to continue? (y/n): ")
        if repeat=='n' or repeat=='N':
            break