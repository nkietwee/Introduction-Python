# i = 0
# while i <= 5:
#     if i == 1:
#         i+=1  # add
#         continue
#     # if i == 5:
#     #     break
#     print(i)
#     i+=1

# i = 0
# while True:
#     if i == 6:
#         break
#     print(i)
#     i+=2

# while True:
#     txt = input("Enter your text : ")
#     if txt == "EXIT":
#         break
# print("Finish")

# try : 
#     nbr = int(input("Enter your number : "))
#     print(nbr)
# except ValueError:
#     print("Can't change data type")
# except:
#     print("Error")

i = 0
while i < 5:
    j = 0
    while j < 10:
        print(i, end=" ")
        j+=1
    print()
    i+=1