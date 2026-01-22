# Common List Patterns
    #print(list(range(start,stop))) >> print(list(range(1,100)))
    #new_sentence = ''.join(['hi', 'my', 'name', 'is', 'Rocky'])
    #print(new_sentence) >>> hi my name is Rocky
# List Unpacking
    #a,b,c = [1,2,3]
        #print(a) >>> 1
    #a,b,c, *other = [1,2,3,4,5,6,7,8]
        #print(other) >>> 4,5,6,7,8
    #a,b,c, *other, d = [1,2,3,4,5,6,7,8]
        #print(other) >>> 4,5,6,7
        #d is now equal to 8. If I did d, e >>> d would be 7 and e would be 8. Other would be 4,5,6
# None (Special Data Type)
    #The Absence of Value
        #weapons = None
            #print(weapons) >>> None
# Dictionary (Data Type and Data Structure)
    #dict
    #A way to help organize data. uses curly brackets {}
    #Lists are easily ordered. Dictionaries are unordered key:value pairs
        #Uses a Key:Value Pair
        #dictionary = {
            #'a': [1,2,3],
            #'b': 2
        #}
            #print(dictionary['b']) >>> 2           
                #This finds the value of b
            #Each Key can have a value of strings, lists, numbers, Booleans, etc
        #my_list = [
            #{
            #'a': [1,2,3],
            #'b': 'hello'
            #},
            #{
            #'a': [4,5,6],
            #'b': 'goodbye'
            #}
            #]
                #If I want to grab the 5 in the second dict I would write:
                #print(my_list[1]['a'][1]) >>> 5

#Developer Fundamentals III (Understanding Data Structures)
    #When to use which data structures
    #Use lists when you need extreme order.
        #Lists only have a single value. Just an index and value  
    #Use dict when you need to pull info not necessarily in order (i.e. Video Games)
        #Dictionaries hold more information!

#Dictionary Keys
    #Don't have to use strings. Can use Booleans, Tuples, and Numbers
    #Keys need to be immutable(Values that cannot change)
    #Keys have to be unique. Can't reuse for other parts of the Dictionary.

#Dictionary Methods
    #user = {
        #'basket': [1,2,3],
        #'greet': 'Good Morning'
    #}
        #print(user.get['age']) >>> None >>> Show's there is no age in user
            #print(user.get('age',55)) >>> 55
                #Shows that if there is no age in the user value, use 55. 
                #If there is an age key, it will use that instead.
    #user2 = dict(name='Rocky') 
        #print(user2) >>> {'name': 'Rocky'}
    #print('greet' in user) >>> True since greet is a key in the user value
    #print('greet' in user.keys()) >>> True. Checks the Keys for greet
    #print('greet' in user.values()) >>> False. Checks the values for greet.
    #print('Good Morning' in user.values()) >>> True

    #print(user.items()) >>> ([('basket', [1,2,3]), ('greet', 'Good Morning')])
        #prints all items in a Tuple ^^^^^
    #print(user.clear()) >>> Empties the Dictionary
        #user.clear()
        #print(user) >>> {} <<< Empties it as well
    #user2 = user.copy() >>> Copies the dict and puts it in user 2. 
    #print(user.pop('basket')) >>> Returns the value of what got removed.
        #Also removes the key basket. 

    #print(user.popitem()) >>> Removes the last key:value pair that was inserted in the dictionary.
    #print(user.update({'greet':'Hello'})) >>> Updates the 'greet' key with a value of 'Hello'

# Tuples 
    #Similar to lists, but immutable(cannot modify)
    #my_tuple = (1,2,3,4,5) <<<< Uses Brackets ()
    #print(5 in my_tuple) >>> True
    #my_tuple[1] = 'z' >>> Will throw an error because we CANNOT change anything within the tuple
    #Less flexible than a list; however, they are more performative (faster)

    #**Tuples ARE valid Keys in a dictionary** 
        #user = {
            #(1,2): 1,2,3,
            #'greet': 'hello'
        #}
    #print(user[(1,2)]) >>> 1,2,3

    #my_tuple = (1,2,3,4)
    #new_tuple = my_tuple[1:2] >>> (2,)        >>>>>>>>>>my_tuple[1:3] >>>> (2,3)
        #[start:stop]
    #x,y,z, *other = (1,2,3,4,5) >>> Still works the same. x=1; y=2; z=3; other=[4,5] << In a list
   #Tuple Methods >>> Only use count() and index()
   # print(my_tuple.count(5)) >>> 1 >>> Counts how many times 5 occurs in the tuple
   #print(my_tuple.index(3)) >>> 4 >>> Shows what is at an index of 3
   # Can also use len() >>> print(len(my_tuple)) >>> 5 >>> counts how many items are in the tuple 

# Sets 
    #Unordered collections of UNIQUE options >>> Uses curly brackets {} with values inside. >>> {1,2,3,4,5}  
    # my_set = {1,1,2,3,4,4,4,4,5}
    # print(my_set)  >>>> {1,2,3,4,5} >>> Only prints the Unique value(1 of each)
    #my_set.add(2)   >>>> print(my_set) >>>> Still outputs {1,2,3,4,5} since 2 is already in there
    #my_set.add(100) >>> print(my_set) >>> {1,2,3,4,5,100}
#my_list = [1,2,3,4,5,5,5,5]
#my_set = set(my_list)                  <<<<<<<<<<<<<< Lines 111-113 is how to print a list with no duplicates involved.
#print(my_set) >>> {1,2,3,4,5}

    #Easier way to do this ^^^ *** is print(set(my_list)) ***
    #Set objects does not support indexing >> print(my_set[0]) << This will throw an error
        #To check to see if a value is in the set >> print(1 in my_set) >>> Outputs True
    #print(len(my_set)) counts each unique value in the set >>> {1,2,3,4,4,5,5} >>> The length would be 5 because there are 5 unique values
    #We can also convert a set into a list with print(list(my_set)) >>> Will make a list of all unique values

# Set Methods
    #.difference() ; .discard() ; .difference_update() ; .intersection() ; .isdisjoint() ; .issubset() ; .issuperset() ; .union() >>> There's a bunch more
#Example sets for usecase of these methods
    #my_set = {1,2,3,4,5}
    #your_set = {4,5,6,7,8,9,10}             >>>>>>>>> Sets are vary useful when comparing 2 sets together

    #print(my_set.difference(your_set)) >>>> outputs {1,2,3} Will show the difference between my_set and your_set. 
        #Both sets contain {4,5} so it won't print those
    #my_set.discard(5)  >>>> print(my_set)  >>> outputs {1,2,3,4} because it discarded(removed) 5 from the set
    #my_set.difference_update(your_set)  >>> print(my_set) >>> outputs {1,2,3} because it updates it by removing the same values between the sets
    #print(my_set.intersection(your_set))  >>> outputs {4,5} because it outputs the common values between the sets
            #print(my_set & your_set)  <<< Does the exact same thing as .intersection()
    #print(my_set.isdisjoint(your_set)) >>> Outputs False because they have values that are the same. If they had no similar values, it would print True
    #print(my_set.issubset(your_set)) >>> will print False because the entirety of my_set is not included in your_set
    #print(my_set.issuperset(your_set)) >>> will print False because my_set does not encompass your_set (Everything in your_set is not in my_set)
    #print(my_set.union(your_set)) >>> outputs {1,2,3,4,5,6,7,8,9,10}  >>>> It joins the sets together removing all duplicates
            #print(my_set | your_set)  <<< Does the exact same thing as .union()
