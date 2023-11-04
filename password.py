#password acceptance

print("Hello User \n")
name = input("Enter your password: ")


while name != "Master12":
    print("Try Again \n")
    name = input("Enter your password: ")
    if (name == "Master12"):
        print("Correct \n")
        break


