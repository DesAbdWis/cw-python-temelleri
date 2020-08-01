counter = 0
# try:
#     with open("rumi.txt", "r", encoding="utf-8") as file:
#         print(file.read())
# except FileNotFoundError:
#     counter += 1
#     with open("hata.txt", "a", encoding="utf-8") as file2:
#         file2.write("Hatali giriş sayısı :" + str(counter) + "\n")
#     print("Böyle bir dosya yok.Hatalı okuma kaydedildi.")

# try:
#     print("x" + 4)
# except TypeError:
#     print("Değer yanlış")
# else:
#     print("Demekki hata yükselmedi")
# finally:
#     print("Kodumuz sonunda çalıştı.")

# while True:
#     no_one = int(input("The first number please : "))
#     no_two = int(input("The second number please : "))
#     try:
#         division = no_one / no_two  # normal part of the program
#     except ZeroDivisionError:
#         print("You can’t divide by zero! Try again.")  # executes when division by zero
#     else:
#         print("The result of the division is : ", division)  # executes if there is no exception
#     finally:
#         print("Thanks for using our mini divison calculator! Come again!")
#         break  # exits the while loop

# while True:
#     no_one = int(input("The first number please : "))
#     no_two = int(input("The second number please : "))
#     try:
#         division = no_one / no_two
#         print("The result of the division is : ", division)
#         break
#     except Exception as e:
#         print("Something went wrong...Try again.")
#         print("Probably it is because of '{}' error".format(e))
#         break

# try:
#     isim = input("İsminiz :")
#     a
    
# except Exception as s:
#     with open ("hata2.txt", "a", encoding="utf-8") as sahin:
#         sahin.write(isim + ","+ str(e) + "\n")

# try:
#     isim = input("isminiz: ")
#     a
# except Exception as e:
#     with open("hata2.txt", "a",) as sahin :
#         sahin.write(isim + "," + str(e) + "\n")

# while True:
#     try:
#         fruit=['banana(0)','mango(1)','pear(2)','apple(3)','kiwi(4)','grape(5)']
#         x=int(input('select your favorite fruit number from list:'))
#         print('my favorite fruit {}'.format(fruit[x]))
#     except (TypeError,SyntaxError,IndexError):
#         print('something is wrong')
#     else:
#         print('everything is okey')
#     finally:
#         break


while True:
    try:
        fruit=['banana(0)','mango(1)','pear(2)','apple(3)','kiwi(4)','grape(5)']
        x=int(input('select your favorite fruit number from list:'))
        print('my favorite fruit {}'.format(fruit[x]))
    except (TypeError,SyntaxError,IndexError):
        print('something is wrong')
    else:
        print('everything is okey')
    finally:
        break