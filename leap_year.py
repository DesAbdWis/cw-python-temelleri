year = int(input("Please enter the 4-digit year you want to find out whether it is a leap year or not : "))
leap_year1 = year % 4 == 0 
leap_year2 = year % 400 == 0
leap_year = leap_year1 and leap_year2
print( leap_year, '\n'+ "(True means the entered year is a leap year )" +'\n'+ "(False means means the entered year is not a leap year)") 