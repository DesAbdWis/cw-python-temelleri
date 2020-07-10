text = ["zero", "one", "two", "three", "four", "five" ]
number = [0, 1, 2, 3]

for i, j in zip(number,text):
    print(i, ":", j)
    print(f"{i} : {j}")
    print("{} : {}".format(i,j))
