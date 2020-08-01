#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code that calculates the average of scores that students took in a math class at below.
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}
ANSWER:
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}
average = sum(scores.values()) / len(scores)
print(average)

#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code that calculates the average of scores that students took in a math class at below.
scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}

#micro-learning
#daily-python-challenge
QUESTION:
Please reverse the text below without using text index methods. Please use a loop.
text = “Clarusway”
ANSWER:
text = "Clarusway"
newtext = ""
for i in range(len(text)-1, -1, -1):
   newtext += text[i]
print(newtext)

#daily-python-challenge
Write a code to calculate factorial of a number entered by user.
#daily-python-challenge
Q:Write a code to calculate factorial of a number entered by user.
A:
number = int(input("Please enter a number : "))
factorial = 1
for i in range(1,number+1):
    factorial *= i
print(f"Factorial of {number} is {factorial}")

#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code to get lengths of a triangle from a user and then check them whether this triangle is equilateral, isosceles or scalene.
ANSWER:
print("Please input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
   print("This triangle is an equilateral triangle")
elif x==y or z==x or y==z:
   print("This triangle is an isosceles triangle")
else:
   print("This triangle is a scalene triangle")


#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code to sort the list at below without using .sort() method of list.
elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
Expected output:
[2, 11, 12, 45, 77, 99, 333, 999, 8982]
ANSWER:
mylist = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
for i in range(len(mylist)):
   for j in range(i+1,len(mylist)):
       if mylist[i] > mylist[j]:
           temp = mylist[i]
           mylist[i] = mylist[j]
           mylist[j] = temp
print(mylist)

#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code that counts how many vowels and constants a string has that a user entered.
ANSWER:
text = input("Please enter a string : ").lower()
constants = 0
vowels = 0
for i in range(len(text)):
   if text[i] in set("aeıioöuü"):
       vowels += 1
   elif text[i] in set("bcçdfgğhjklmnpqrsştwxyz"):
       constants += 1
print(f"Your text has {vowels} vowels and {constants} constants")

#micro-learning
#daily-python-challenge
QUESTION:
Write a Python code to get lengths of a triangle from a user and then check them whether this triangle is equilateral, isosceles or scalene.
ANSWER:
print("Please input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
   print("This triangle is an equilateral triangle")
elif x==y or z==x or y==z:
   print("This triangle is an isosceles triangle")
else:
   print("This triangle is a scalene triangle")

#daily-python-challenge
Define a “function” to calculate permutation of 2 numbers.
Reminder: P(n,r) = n!/(n-r)!
Clue: Defining a function that calculates factorial of given number, may be helpful.

#daily-python-challenge
Question:
Define a “function” to calculate permutation of 2 numbers.
Reminder: P(n,r) = n!/(n-r)!
Clue: Defining a function that calculates factorial of given number, may be helpful.
Answer:
def factorial(number):
   fact = 1
   for i in range(1,number+1):
       fact *= i
   return fact
def permutation(n,r):
   return int(factorial(n)/factorial(n-r))
n = int(input("To calculate permutation please enter n : "))
r = int(input("To calculate permutation please enter r : "))
print(f"Permutation of ({n},{r}) is {permutation(n,r)}")



#daily-python-challenge
# Write a Python code that finds the students who have maximum and minimum average at a given dictionary below.
{'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}

#daily-python-challenge
Question:
Write a Python code that finds the students who have maximum and minimum average at given dictionary below.
Answer:
scores = {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, \
'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, \
'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, \
'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, \
'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}
maxavr, minavr = 0, 100
for i in scores:
   average = sum(scores[i].values())/len(scores[i].values())
   if average > maxavr:
       maxavr = average
       maxkey = i
   if minavr > average:
       minavr = average
       minkey = i
   print(f"{i}   {average:.1f}")
print(f"\n{maxkey} has maximum average with a score {maxavr}\n{minkey} has minimum average with a score {minavr}")