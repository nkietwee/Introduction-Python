def login(*, username, password):
    print(f"Username: {username}")
    print(f"Password: {password}")

usr = input("Enter username: ")
pwd = input("Enter password: ")
login(username=usr, password=pwd)