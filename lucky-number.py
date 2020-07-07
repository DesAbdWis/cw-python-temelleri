number = 27

a = int(input("please try to estimate my number : "))
while True :
    if a > number:
        print("your number is bigger.")
        a = int(input("please try to estimate my number : "))
    elif a < number:
        print("your number is small")
        a = int(input("please try to estimate my number : "))
    else:
        print("your number is right.")

        print(" are you mindreader")
        break
    