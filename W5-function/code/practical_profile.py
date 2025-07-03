def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

show_profile(name=name, age=age, city=city)
