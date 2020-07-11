limit = int(input("Please enter limit number findout fibonnaci numbers : "))
list = []
f_numbers, increase = 0, 1
while f_numbers <= limit:
    list.append(f_numbers)
    print(list)
    f_numbers, increase =  increase, f_numbers + increase
