import string
alphabets = string.ascii_lowercase
n = input("Enter a string: ")
flag = 0
for i in alphabets:
  if(i not in n):
    break
  else:
    flag = flag + 1
if(flag == 26):
  print("It is a pangram")
else:
  print("It is not a pangram")