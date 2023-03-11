l = []
n = int(input("Enter the number of students: "))
for i in range(n):
    l.append(tuple(x for x in input("Enter the student roll no., name, marks: ").split()))
print(l)
name = input("Enter name: ")
for i in l:
    if name in i:
        print("Student Details: ",i)
        break
    else:
        print("Student not found")