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

#December 18,2025

#Escape Sequences
    #Weekday = 'It's Sunny' << Can't do that because the apostrophe stops the string
        #Do this instead >> Weekday = 'It\'s Sunny'
        #The Backslash tells python that whatever comes after it is a string. 
    #Weekday = '\t It\'s Sunny'
        #The \t adds a tab spacing to the string
    #\n adds a new line. 
#Formatted Strings
    #name = "Brandon"
    #print('Hi ' + name) >>> Hi Brandon
    #Easier way to do >> print(f'Hi {name}')
        #adding f to the beginning shows we're going to use a formatted string. Then use brackers {} for variables. 
    #Python 2 used print('Hi {}, you are {} years old.'.format('Brandon', '30'))
        # or print('hi {}'.format(name))
    #print(f'')is the preferred method
#String Indexes
    #movie = 'My name is Inigo Montoya'
    #         0123456789..............>>>>
        #Each shelf corresponds to a value. M=0 1=y and so on
        #print(movie[0]) >>> Outputs M. 
        #print(movie[11]) >>> Outputs I
    #Indexes always start with 0!
    # **USE SQUARE BRACKETS [] FOR INDEXES**
    #[start:stop]
    #print(movie[0:5])
        #Counts to the fifth number. 0,1,2,3,4. 
            #Outputs >>> My na
    #[start:stop:stepover] >>> Called String Slicing***
        #stepover default is 1 because we are going 1 by 1
        # if we do print(movie[0:9:2]) it outputs M nm i because it stepsover by 2
    #print(movie[1:]) >>> Makes it to where it doesnt stop
    #Defaults are always [Beginning:End:1]
    #print(movie[-1]) outputs a. It starts at the end
    #print (movie[::-1]) reversed the string. 
#Immutability
    #Strings in Python are immutable
    #movie[0] = 'N' >>>Won't change the M in My because I can't change anything within the string.
#Built-in Functions + Methods
    #str(); int(); print() >>> These are functions
    #len() Calculates the length of the string. 
        #len() does not count from 0 like indexing does.
        # movie = "My name is Inigo Montoya"
        # print(len(movie)) = 24. len() does count spaces and punctuation!
    #Methods are similar to functions but owned by something. 
        #Methods usually have a . in front and then a word. >> .format is a method.
        #quote = "to be or not to be"
            #print(quote.upper()) >>> Capitalizes everything 
                #TO BE OR NOT TO BE
            #print(quote.capitalize()) >>> Just capitalizes the start of the string.
                #To be or not to be
            #print(quote.find('be')) >>> outputs 3 because 'be' starts at the index of 3.
                #Finds the first occurance.
            #print(quote.replace('be','me')) >>> to me or not to me
                #replaces all instances of be to me. .replace(word to be replaced, word to replace it with)

# December 19, 2025

#Booleans
    #bool
        #True/1 or False/0 (Capital T and Capital F)
    #name = "Brandon"
    #will_be_successful = True

#Type Conversion Exercise
    # birth_year = input("What year were you born?")
    # age = 2025 - int(birth_year)
    # print(f"You are {age} years old.")
        # Make sure that I turn birth_year into an integer to be able to subtract it from 2025.

# **Make code that is easy to read and easy to understand**
    # *Only add comments to code if something important is happening that might be a little difficult*

#Password Checker Exercise
# user = input("What is your username?")
# pswd = input("What is your password?")
# pswd_len = len(pswd)
# hidden_pswd = pswd_len * '*'
# print(f"Hello {user}, your password, {hidden_pswd}, is {pswd_len} characters long.")

#Lists
    #li = [1,2,3,4,5] >>> Lists use square brackets
    #li2 = ['a',2,'c',4,'e']
    #Lists are the first data structure I'm learning
        # ** Data Structures are ways to store information **
# target_cart = ['Funko Pops', 'Football Cards', 'Shampoo']
# print(target_cart[1]) >>> Outputs Football Cards. 
    #Like string slicing, the index/list starts with 0 (funko pops)

#List Slicing
'''target_cart = [
'Funko pops',
'Football cards',
'Shampoo',
'Milk'
]'''
#^^^ Formatting lists this way makes things simpler
#List slicing is the same as string slicing with [start:stop:step]
    #Strings were immutable; however, lists are not! We CAN change lists.
#target_cart[0] = 'Laptop'
#print(target_cart)>>> Outputs Laptop, Football cards, Shampoo, Milk
# To copy a list use [:]
    #new_cart = target_cart[:]
#if we do just new_cart = target_cart, then whenever we change anything in new_cart, it'll change the target_cart as well. 

#Matrix
    #A way to describe multidimensional lists.
'''matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]'''
#print(matrix[0][1]) >>> Will output 2. The first item is [1,2,3] and index 1 in that is 2.

#List Methods
    #len() can calculate the length of the list.
    
# li1 = ['legos', 'toys', 'rocks']
    #Adding methods. 
# li1.append('socks') >>> adds socks to the end of the list. 
# print(li1) >>> Shows the list with the new item added.
#li1.insert(2, 'funkos') >>> inserts funkos at an index of 2.
    #.insert(index, new item/object)
#li1.extend([100,'shampoo']) >> adds on or extends the list

    #Removing Methods
#li1.pop()>>> pop pops off whatever is at the end of the list. 
#li1.pop(0)>> removes whatever is at the index of 0
#li1.remove('legos') >>> Will remove the value we give it. 
    #.pop() gets rid of the index while .remove() gets rid of the value
#li2 = li1.pop(2) >>> print(li2) >>> will return the 2nd index of li1(rocks)
#li1.clear() >>> Clears the whole list. 


#print(li1.index('legos')) >> Asks what index legos is in >> will output 0
#.index(value, start, stop) >>> .index('legos', 0, 3) >>> Searches between index 0 and 3
    #another way to find out >> print('legos' in li1) >>> True
#print(li1.count('legos')) >>> Will output 1 because legos only occurs once in the list. 
#li1.sort() >>> print(li1) >>> Will sort the list alphabetically.
#print(sorted(li1)) >>> Does the same thing but it produces a new array. Makes a new copy. 
#li2 = li1.copy() >> Copies the lists onto li2
#li1.reverse() >>> print(li1) >> Reverses the li1 in place

