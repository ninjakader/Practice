#password acceptance


name = input("Enter the password: ")


while name != "Master12":
    print("Try Again \n")
    name = input("Enter the password: ")
    if (name == "Master12"):
        print("Correct \n")
        break


