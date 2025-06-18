
try :
    total = int(input("Enter your grade : "))

    if total >= 90 and total <= 100:
        print("Your Grade is A")
    elif total >= 80 and total < 90:
        print("Your Grade is B")
    elif total >= 70 and total < 80:
        print("Your Grade is C")
    elif total >= 60 and total < 70:
        print("Your Grade is D")
    else:
        print("Your Grade is F")
except ValueError:
    print("Invalid input! Please enter integers only.")