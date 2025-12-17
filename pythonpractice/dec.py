#Dec 15, 2025

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

#Operator Precedence
    # 20 + 3 * 4 << It's going to do the multiplication first. 
    # Similar to PEMDAS
    # Order >> () , ** , */ , +-

#Complex (Data Type)
    # A third type of number along side of int and float
    # Not often used
# Bin() 
    #Returns the binary interpretation of a number
    #print(bin(5)) >>> 0b101
        #0b tells python its a binary number. The binary number for 5 is 101.
    # print(int('0b101', 2)) >>> Turns the Binary back to an integer. 

#December 16, 2025

#Variables
    #Stores info that can be used in our program
    #birth_month = "May" >> birth_month is the variable
    #print(birth_month) >> May
        #binding the month May to the variable birth_month

    #Variable Rules
        #snake_case
        #Start with a lowercase or underscore
        #Letters, numbers, underscores
        #Case Sensitive
        #Don't overwrite keywords (i.e. print, else, return)
    #Variables can be assigned
#constants
    #PI = 3.14
        #Making PI all caps like this shows other programs it should be constant and shouldn't be changed.
# __   <<<< Two underscores is called a Dunder.

#Make my code readable and understandable by other programmers
#a,b,c = 1,2,3 <<< Allows me to assign values to multiple variables at once

#Expressions vs Statements
    #year = 2025
    #age = 30
    #birth_year = year - age   <<< year - age is an expression because it produces a value
        #the whole line >>birth_year = year - age<< is a statement because its an entire line of code that performs some type of action

#Augmented Assignment Operator
    #a_value = 5 >> If printed outputs 5
    #a_value += 2 >> If printed outputs 7 because 2 is added to 5
    #can use += ; -= ; *= ; /= ; ** ; // ; %

#Strings
    #Can use '' or ""
    #A piece of text. Can put anything in a string
    #long_string = ''' ..... ''' Will allow for multiple lines of strings
 
    #f_name = 'Brandon '
    #l_name = 'Tyhurst'
    #full_name = f_name + l_name
    #print(full_name) >> Outputs Brandon Tyhurst
#String concatenation
    #Adding strings together
    #print('Hello ' + 'Brandon') >> outputs Hello Brandon

#Type Conversion
    #100 is an int, but if we do print(str(100)) >> the output is 100 still but the type is str
    #print(int(30.0)) >> outputs 30 because it turns the float of 30.0 into an int
