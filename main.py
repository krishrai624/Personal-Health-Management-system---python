print("Welcome to Health Management system.\n")
def getdata():
    import datetime
    return datetime.datetime.now()

def log(a):
    if a == 1:
        treatment = int(input("Enter exercise for 1 and food for 2:"))
        if treatment == 1:
            item = input("Exercise you want:")
            with open("harry exercise.txt","a") as file:
                file.write(str(getdata())+" is "+item+"\n")
            print("You have added an exercise item.\n")
        elif treatment == 2:
            item = input("Food you eat:")
            with open("harry food.txt","a")as file:
                file.write(str(getdata())+" is "+item+"\n")
            print("You have added an food item.\n")
        else:
            print("You have enter invalid number. Please! try again while typing exercise for 1 and food for 2")

    elif a == 2:
        treatment = int(input("Enter exercise for 1 and food for 2:"))
        if treatment == 1:
            item = input("Exercise you want:")
            with open("rohan exercise.txt", "a") as file:
                file.write(str(getdata())+" is "+item+"\n")
            print("You have added an exercise item.\n")
        elif treatment == 2:
            item = input("Food you want:")
            with open("rohan food.txt","a") as file:
                file.write(str(getdata())+" is "+item+"\n")
            print("You have added an food item.\n")
        else:
            print("You have enter invalid number. Please! try again while typing exercise for 1 and food for 2")

    elif a == 3:
        treatment = int(input("Enter exercise for 1 and food for 2:"))
        if treatment == 1:
            item = input("Exercise you want:")
            with open("hammad exercise.txt","a") as file:
                file.write(str(getdata())+" is "+item+"\n")
            print("You have added an exercise item.\n")
        elif treatment == 2:
            item = input("Food you want:")
            with open("hammad food.txt","a")as file:
                file.write(str(getdata())+" is "+item+"\n")
            print("You have added an food item\n")
        else:
            print("You have enter invalid number. Please! try again while typing exercise for 1 and food for 2")

    else:
        print("You have enter invalid number!!!\nPlease! enter the number Harry for 1, Rohan for 2 and hammad for 3.\n")

def retreive(a):
    if a == 1:
        treatment = int(input("Enter exercise for 1 and food for 2:"))
        if treatment == 1:
            with open("harry exercise.txt")as file:
                for i in file:
                    print(i, end="")
        elif treatment == 2:
            with open("harry food.txt")as file:
                for i in file:
                    print(i, end="")
    elif a == 2:
        treatment = int(input("Enter exercise for 1 and food for 2:"))
        if treatment == 1:
            with open("rohan exercise.txt")as file:
                for i in file:
                    print(i, end="")
        elif treatment == 2:
            with open("rohan food.txt")as file:
                for i in file:
                    print(i, end="")
    elif a == 3:
        treatment = int(input("Enter exercise for 1 and food for 2:"))
        if treatment == 1:
            with open("hammad exercise.txt")as file:
                for i in file:
                    print(i, end="")
        elif treatment == 2:
            with open("hammad food.txt")as file:
                for i in file:
                    print(i, end="")
    else:
        print("You have enter invalid number!!!\nPlease! enter the number Harry for 1, Rohan for 2 and hammad for 3.\n")
while(True):
    print("To choose client: Harry for 1, Rohan for 2 and Hammad for 3")
    a = int(input("Press 0 to exit.\nEnter log for 1 and retrieve for 2:"))
    if a == 1:
        if a == 1:
            client = int(input("Choose the client number:"))
            log(client)
        else:
            client = int(input("Choose the client number:"))
            retreive(client)
    elif a == 2:
        if a == 1:
            client = int(input("Choose the client number:"))
            log(client)
        else:
            client = int(input("Choose the client number:"))
            retreive(client)
    elif a == 0:
        print("You quit.")
        break
    else:
        print("Please, try again!!!\n")

# I have to make this 0 to end this code.
