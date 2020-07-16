numb = int(input("Please enter positive number to know factorial : "))

factorial_numb = 1
for i in range(1,(numb+1)):
    factorial_numb *= i
print(f"The factorial of {numb} is, {factorial_numb}")


