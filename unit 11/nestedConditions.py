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
    pin =int(input("please enter your pin number"))
    account = 200
    pinNumber = 1234
    if pin == pinNumber:
       
       print("welcome, what would you like to do? ")
