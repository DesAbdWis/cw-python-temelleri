while True:
    number = input("enter a positive number :")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "It is an invalid entry. Don't \
        use non-numeric, float, or negative values!")
    elif int(number) >= 0:
        for i in range(digits):
            summ += int(number[i]) ** digits
        if summ == int(number):
            print(number, "is an Armstrong number.")
            break
        else:
            print(number, "is not an Armstrong number.")
            break