sentence = input("Please enter a sentence for counting the number of each letter in your sentence : ")
letter_number = {}

for i in sentence:
    if i in letter_number:
        letter_number[i] += 1
           
    else:
        letter_number[i] = 1
   
print(str(letter_number))

