toSort = input("Enter a string: ")
words = toSort.split()
words.sort()
for word in words:
 print(word, end=' ')
to_check_palindrome = input("\nString: ")
if(to_check_palindrome == to_check_palindrome[:: -1]):
 print( f'{to_check_palindrome} is Palindrome')
else:
 print(f'{to_check_palindrome} is Not a Palindrome')