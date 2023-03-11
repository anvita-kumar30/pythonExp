year=int(input("Enter the year to be checked: "))
if((year % 400 == 0) and (year % 100 == 0)):
        print("{0} is a leap year".format(year))
elif((year % 4 ==0) and (year % 100 != 0)):
        print("{0} is a leap year".format(year))
else:
        print("{0} is NOT a leap year".format(year))
