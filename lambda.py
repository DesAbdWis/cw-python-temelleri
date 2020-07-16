numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x**2, numbers)
print(list(result)) 
print()
print()
def square(n):
    return n**2
numbers = [1, 2, 3, 4, 5, 6]
result = map(square,numbers)
print(list(result)) 

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = [7, 8, 9]
result = map(lambda x,y,z: x+y+z, num1,num2,num3)
print(list(result))

number_list = [1, 2, 3, 4, 5]

result = list(map(lambda x : x*3, number_list))
print(list(result))

number_list = [1, 2, 3, 4, 5]
def triple (n):
    return n*3
print(list(map(triple,number_list)))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
filtre = filter(lambda i:i%2==0, numbers)
print(list(filtre))


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
def even(x):
    return x%2==0
filtre2 = filter(even,numbers)
print(list(filtre2))

vowel_list = ['a', 'e', 'i', 'o', 'u']
sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vowels = filter(lambda x: True if x in vowel_list else False, sentence)
print("Vowel letters in sentence are", list(vowels))

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x >= 6, number_list)
print(list(result))


def sayi_kuvveti(n):
    return lambda x: x**n
sayi_kuvveti_2 = sayi_kuvveti(2)
sayi_kuvveti_3 = sayi_kuvveti(3)
sayi_kuvveti_4 = sayi_kuvveti(4)

print(sayi_kuvveti_2(9))
print(sayi_kuvveti_3(5))
print(sayi_kuvveti_4(4))

def modular_function(n):
    return lambda x: x ** n

power_of_3 = modular_function(3)
print(power_of_3(5))

print((lambda x: x**3)(5))

multiply = lambda x: x * 4
add = lambda x, y: x + y
print(add(multiply(10), 5))


sum_double = lambda x,y: x+y
print(sum_double(1, 2))

sum_double = lambda x,y: x+y if x!=y else 2*(x+y)
print(sum_double(1, 2))
print(sum_double(5, 5))



