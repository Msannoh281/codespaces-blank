# While Loops definition - a while loop is a type of constract
# where code instructions will keep on running so'
# long as a condition is TRUE (boolean)

# NOTE - In order to stop a loop (or any program) from running
# in your terminal, click ctrl +c at the same time.

# While loop syntax 
def ageVerify():
videoGameAge = 17
purchaserAge = 15 = int(input('how old arew you?'))

while videoGameAge > purchaserAge: # this is a true statement
    print('You are not old enough to buy this game')
else:
       print("Cool, you can buy this game.")

savedPw = '123abc'
userPw = input("please enter your pw: ")
attempt = 0
while savedPw 1= userPw:
    print("incorrect pw. Try again: ")
    print(attempt)
    attempt +=1 
    userPw = input('Please type your password again:')

else:
     print("welcome to your account")
