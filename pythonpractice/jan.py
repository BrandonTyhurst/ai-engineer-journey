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


