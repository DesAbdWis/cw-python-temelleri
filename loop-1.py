ps4_price = 40 
x = int(ps4_price/2) 
saved_amount = int(input('Please enter your saved amount: '))
if x <= saved_amount:
    print("You must save more, keep saving!")
elif x >= saved_amount:
    print("You saved more than half, keep saving!")
else :
    print("Yippee! You can buy your PS4")