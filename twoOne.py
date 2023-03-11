import array as arr
array=arr.array('i',[])
n=int(input("Enter size of array: "))
for i in range(n):
    array.append(int(input(f"Enter {i+1} element: ")))
print("Entered Array: ")
for i in range(n):
    print(array[i])
array.append(int(input("Enter the element you want to append at the end: ")))
print("Entered Array: ")
for i in range(len(array)):
    print(array[i])
print("Array after Reversing: ")
RevArr=array[::-1]
for i in range(len(RevArr)):
    print(RevArr[i])
print(f"Length in bytes of one Array item : {str(array.itemsize)}\n")
print("Enter another 2nd Array: ")
array2=arr.array('i',[])
n=int(input("Enter size of array: "))
for i in range(n):
    array2.append(int(input(f"Enter {i+1} element: ")))
for length in range(len(array2)):
    array.append((array2[length]))
print("Array After appending the 2nd Array")
for i in range(len(array)):
    print(array[i])

array.pop(int(input("Enter the index of array element you want to remove: ")))
print("Array after popping the element: ")
for i in range(len(array)):
    print(array[i])
index=int(input("Enter the index where element should be inserted: "))
value=int(input("Enter Element: "))
array.insert(index,value)
print("Array after inserting the element: ")
for i in range(len(array)):
    print(array[i])
print("Array after converting to String is: ")
toString=''.join(str(a) for a in array)
print(toString)