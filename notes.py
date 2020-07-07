notes = int(input("please enter your note : "))

if notes > 90:
    if notes >= 95:
        print("A+")
    else:
        print("A")
elif notes >= 80 and notes < 90 :
    if notes >=85:
        print("B+")
    else :
        print("B")
else :
    print("Below B")