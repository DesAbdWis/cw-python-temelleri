with open("people.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.read(file, delimiter= ",")  
    for row in csv_rows: 
        print(row) 
