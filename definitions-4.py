def calculator (a, b, ope ) :
    if ope == "+":
        return(a+b)
    elif ope == "-":
        return(a-b)
    elif ope == "*":
        print(a*b)
    elif ope =="/":
        return(a/b)
    else:
        return("enter valid number / operator")
   
   
calculator(15,2, "+")
print(calculator(15,2, "+"))