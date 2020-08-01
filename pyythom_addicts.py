try:
    with open("deneme.txt", "r", encoding="utf-8") as file:
        print(file.read())
except:
    print("file doesn't found")