number = int(input("Please enter a positive number : "))
if number == 0:
    print("Zero is not prime number")
elif number == 1:
    print("One is not prime number")
elif number == 2:
    print("Two is prime number")
else:
    for i in range (2,6):
        if number %i == 0 :
            print(f"The {number} is not prime number. Because {number} is divived by {i} ")
            break
    else:
        print(f"The {number} is prime number.")
