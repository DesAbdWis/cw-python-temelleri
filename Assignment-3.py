number = input("Please enter a positive number : ")

if float(number) < 0:
    print("Please enter a positive number")
    
elif isinstance(number, float) == True:
    print("Please enter a positive integer number")
    

else:
    power_of_number = len(number)
    armstrong_number = 0
    for i in number:
        armstrong_number += int(i)**int(power_of_number)
  
    if int(number) == int(armstrong_number):
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")
