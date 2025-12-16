# print ('Brandon T')
# name = input('What is your name?')
# print('Hello ' + name)
    #If I type in Brandon when it asks my name, it'll say Hello Brandon

#Python Fundamental Data Types
    # int
    # float
    # bool
    # str
    # list
    # tuple
    # set
    # dict

#Classes --> Custom Types

#Specialized Data Types
    #Modules ^^

#None (Means nothing. Absence of Value. <<A Data type<<)


#numbers (int and float)
    #int>>integer
        #A Whole Number with no decimal point. Positive or Negative
# print(2 + 4)
# + Add; - Subract; * Multiply; / Divide
#Can check the type of Data Type with print(type(2 + 4))
# print(type(2 + 4))
# print(type(2.0 + 4.0))

#Print(type(2.0 + 4.0)) >>> Prints Float because it is a floating point number
    #A float is any number that contains a decimal point. (3.14159; 1.1; 2.0)
    #A float takes up much more space in memory than an integer does. 

#print(2 ** 3) >> The ** means to the power of. So the output would be 8 since 2 to the power of 3 = 8
#print(81 // 8) >> This does 81 divided by 8 but then rounds down to an integer
    # 81 divided by 8 = 10.125. So the output of print(81 // 8) would be 10
#print(5 % 4) >> Asks what the remainder of this division is.
    # 5 divided by 4 is 1 1/4. So the remainder is 1 which is what the output would be.

# Math Functions
    #print(round(3.14159))
        # ^^ Round is a function that rounds the float to the nearest integer.
        # So the output of the above print would be 3
    #print(abs(-10))
        # ^^ abs returns the absolute value of a number.
        # The output of the above print would be 10

## Developer Fundamentals **IMPORTANT** 
    #Don't read the Dictionary.
        #Don't try to memorize every single thing such as functions, syntaxes, etc
        #Know what exists and can be used. It's ok to google something if I'm unsure of it. 

name = input('What is your name?')
if len(name) == 5:
    print('You are allowed to be here')
if len(name) == 6:
    print('Go Away')
if len(name) > 6: 
    print('Get Rick Rolled')