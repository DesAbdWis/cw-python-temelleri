n = int(input("enter a number to check if it is a prime or not:"))
list_not_prime = []
list_prime = []

for i in range(1, n+1) :
    if not (n % i) : 
        count += 1
if (n == 0) or (n == 1) or (count >=3) : 
    list_not_prime.append(n)

else :
    list_prime.append(n) 

print(list_prime)
print(list_not_prime)