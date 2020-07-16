number = int(input(
    "Please enter a positive number whether to find out prime number or not : "))

list_prime = [2]

for i in range(2, number + 1):
    if i > 1:
        for n in range(2, i//2 + 2):
            if (i % n) == 0:

                break
            else:
                if n == i//2 + 1:
                    list_prime.append(i)

print(list_prime)
