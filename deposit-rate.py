p = input ("Please enter your deposit amount= "'\t')
r = input ("Please enter fix daily profit rate (% ?) = " '\t')
i = int(r)/100
n = input ("Please enter day number (1 or 5 etc...) = " '\t')
a = int(p)*(1+float(i))**int(n)
print("Your total amount of deposit is = " '\t')
print(round(a, 4))