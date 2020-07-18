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