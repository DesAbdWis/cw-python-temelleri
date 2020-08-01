sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

def insert(list):
    lenlist = len(list)
    i = 0
    j = 3
    while j < lenlist:
        list.insert(j+i, "|")
        i += 1
        j += 3
    return list
a = ("- " * 16)

for i in range(len(sudoku)):
    if i % 3 == 0:
        print(a)
    print(*insert(sudoku[i]), sep=" ")
print(a)