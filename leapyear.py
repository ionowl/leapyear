# Python program to check if year is a leap year or not

year = int(input("Enter a year: "))

if (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))