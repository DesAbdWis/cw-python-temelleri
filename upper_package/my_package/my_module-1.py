
number_list = [1, 2, 3, 4, 5]
def triple (n):
    return n*3
print(list(map(triple,number_list)))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
filtre = filter(lambda i:i%2==0, numbers)
print(list(filtre))