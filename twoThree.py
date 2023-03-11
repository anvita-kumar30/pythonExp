strInput = input("Enter a string: ")
print ("String:"+strInput)
firstChar = strInput[0]
char='@'
length=len(strInput)
if length > 1:
 strInput = strInput[0] + strInput[1: ].replace(firstChar,char)
print("Resulted String: " +strInput +"\n")