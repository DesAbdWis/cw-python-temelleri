rumi = open("rumi.txt", 'r')   

print(rumi.read())  # displays the entire text content

rumi.close()  # be sure to close the file


rumi = open(file = "rumi.txt", mode="r")   

print(rumi.read(35))  
print()
print(rumi.read(13))  
print()
print(rumi.tell())  
print()
rumi.seek(16)  
print(rumi.read(20))
rumi.close()