def signup():
    email =input("please enter email: ")
    password = input("please create a password: ")
    if email == 'hom@mail.com' :
        print("you already have an account")
    else:
        username = input("Welcome! please create a username: ")
        if username == 'ian' :
            print("sorry, that user already exist")
        else:
            print("great your all set")

signup()

def movieTickets():
    age = input("please type ")
    print("1. toys")
    print("2. finding nemo")
    print(". shrek")
    response = input("please select a movie by number")
    if response == 1:
        print("here is your ticket for toys")
    elif response == 2:
        print("here is your ticket for finding nemo")
    elif response == 3:   
        print("here is your ticket for shrek") 


def atm():
    balence = 5000
    pin = 1234
    print("welcome, please type your pin number: ")
    userPin= int(input())
    if userpin == pin:
        print("welcome what would you like to do? ")
        print("1. Withdraw money")
        print("2. depoit money ")
        print("3. check balence")
        select= pin =int(input("please select an option: "))
        if select == 1:
            print('how much would you like to withdraw')
            amount = int(input())
            if amount > balance:
                print("Overdraft a alert")
            else:
                newBalence = balence - amount
                print("you are taking out " + str(amount))
                print("you have this amount left: " + str(newBalence))
   
    elif select == 2:
         print('How much money do you want to deposit?')
         amount = int(input())
         newBalence = balence - amount
         print("you adding to your account: " + str(amount))
         print("your new balence is: " + str(newBalence))

    elif select: