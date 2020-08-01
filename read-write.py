#rumi = open("rumi.txt", 'r',  encoding="utf-8")
#for line in rumi:
 #   print(line[:-1])

#rumi.close()
#print()
#rumi = open("rumi.txt", 'r',  encoding="utf-8")
#for line in rumi.readlines():
 #   print(line, end="")

#rumi.close()

#print()

#with open("rumi.txt", "r", encoding="utf-8") as file:
 #  print(file.read())

# with open("fishes.txt", "r", encoding="utf-8") as file:
  #  print(file.read())
 
# with open("dummy.txt", "w", encoding="utf-8") as file:
   #     file.write("This is my first file.\n")
#with open("dummy.txt", "r", encoding="utf-8") as file:
#    print(file.read())

with open("dummy.txt", "a", encoding="utf-8") as file:
    file.write("This is second line.")
with open("dummy.txt", "r", encoding="utf-8") as file:
    print(file.read())

fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
with open ("fruits.txt", "w", encoding="utf-8") as file:
    for basket in fruits:
        file.write(basket +"\n")

with open("fruits.txt", "r", encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", "r", encoding="utf-8") as file:
    print(file.readlines())


flowers = ["Jasmine", "Rose", "Lily", "Daisy", "Tulip"]

with open ("flowers.txt", "w", encoding="utf-8") as file:
    for basket in flowers:
        file.write(basket +"\n" +"\n")
with open("flowers.txt", "r", encoding="utf-8") as file:
    print(file.readline())





flowers = ["Jasmine\n", "Rose\n", "Lily\n", "Daisy\n", "Tulip\n"]

with open ("flowers.txt", "w", encoding="utf-8") as file:
    file.writelines(flowers)
with open("flowers.txt", "r", encoding="utf-8") as file:
    print(file.read())

fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
with open ("fruits.txt", "a", encoding="utf-8") as file:
    file.write("melon")

with open("fruits.txt", "r", encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", "r", encoding="utf-8") as file:
    print(file.readlines())


flowers = ["Jasmine", "Rose", "Lily", "Daisy", "Tulip"]

with open ("flowers.txt", "a", encoding="utf-8") as file:
    file.write("orchid")
with open("flowers.txt", "r", encoding="utf-8") as file:
    print(file.read())



with open("istiklal.txt", "r", encoding="utf-8") as file:
    print(file.read())



#with open("istiklal.txt", "r", encoding="utf-8") as file:



    #for line in istiklal:
        

#with open("istiklal.txt", "r", encoding="utf-8") as file:
    #print(file.read())

