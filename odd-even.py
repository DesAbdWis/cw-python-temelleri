
print(list(range(0,10,2)))

print(list(range(1,10,2)))

even = []
odd = []

for i in range(10):
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("evens :", even)
print("odds :",odd)


