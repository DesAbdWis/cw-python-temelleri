year = int(input("Please enter the 4-digit year you want to find out whether it is a leap year or not : "))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(f"{year} is a leap year")

else:
    print("{} is not leap year".format(year))