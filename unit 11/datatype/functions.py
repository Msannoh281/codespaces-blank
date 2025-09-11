#






























   print("Here is your result! ")
   print(int(a) + b)



#create a function for calculation numbers
def calculate(): 
    a = input('Please enter a number')
    b = input("Please enter another number: ")
    print(int(a)  + int(b))
    print(int(a)  - int(b))
    print(int(a)  * int(b))
    print(int(a)  / int(b)) 

calculate(10,10)

# functions have a way passing without users
# we can past data through the function parmeters
# the round brackets at the end of a functions are
# are called function parameters. parameters are placeholders for expected
# data
def shoppingCart(items): #items is the parameter /placeholder
    print( "You have " + str(items) + ' items in your carts')

# when data is passed in the function definition,
# it is called an arguement because its using rael data