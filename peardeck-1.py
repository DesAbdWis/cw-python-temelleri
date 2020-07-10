number = int(input("Please enter a number between 1 to 10 : "))
j = 0
while j <= number:
    m = number * j
    print(number,"x",j, "=", m)
    print("{} x {} =".format(number,j), m)
    print(f"{number} x {j} = {m}")
    j += 1

number = int(input("Please enter a number between 1 to 10 : "))
for i in range(11):
    print(number, "x", i, "=", number*i)
    print("{} x {} =".format(number,i), number*i)
    print(f"{number} x {i} = {number*i}")
