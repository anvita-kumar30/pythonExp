import array as arr
array= arr.array('i',[])
notprime = arr.array('i',[])
Elements = int(input("Enter the number of elements : "))
for element in range(Elements):
 array.append(int(input(f'Enter the { element+ 1} Element: ')))
flag= False
print(f'The Array is {array}')
length = len(array)
for element in range(length):
 for j in range(2,array[element]):
  if array[element]%j == 0:
   notprime.append( array[ element])
   break
print("The array after removing all Prime numbers is : ")
print(notprime)