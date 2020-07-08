number = input("Please enter a positive number : ")

if number.isdigit() == True:
    power_of_number = len(number)
    armstrong_number = 0
    for i in number:
        armstrong_number += int(i)**int(power_of_number)
        if int(number) == int(armstrong_number):
            print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")

else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
  
