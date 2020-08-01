# leardic_square = {str(i) +"'in karesi" : i*i for i in range(8)}
# print(dic_square)

# leardic_square = {str(i) +"'in karesi" : i*i for i in range(8)}
# # print(dic_square)
# import csv
# with open ("people.csv", "r", encoding="utf-8") as file:
#     csv_rows = csv.read(file, delimiter= ",")  
#     for row in csv_rows: 
#         print(row) 

# import pandas as pd

# df = pd.read_csv("fruits.csv", index_col = 0)

# print(df)
# xx listesini value değerlerine göre sıralama
# xx = {"e" : 4, "b" :2, "c": 3, "f":1}
# print(sorted(xx.items(), key = lambda x : x[1]))

my_list = [1, 2, 3, 4, 5]
a = max(x**2 for x in my_list)
print(list(a))


