print("Hello World! Pass this test, please.")

        # DATA TYPES IN PYTHON 
# interpreter : a program that executes other programs 
# Python shell : interactive interpreter that can be accessed from the terminal 

                # Strings 
# done with single/ double quotes 
# can also use string constructor-> str("I'm a string")
# to do string interpolation, use an f-string-- works like backticks in js
  # dog_name = "Lucy"
  # print(f"Say hello to my dog, ${dog_name}") ---> Say hello to my dog, Lucy
        
        #EXAMPLES
#/price_1 = 3
#price_2 = 2.5
#print(f"Item 1 costs ${price_1:.2f}")
# => Item 1 costs $3.00
# this works when using f-strings 

# "hello".upper() -> "HELLO"

# "HELLO".lower() -> "hello"

# "hello".capitalize() -> "Hello"

# "hello" + "world" -> "helloworld"

# "hello" * 3 -> "hellohellohello"

# dir() function lists all the available methods that can be used on objects 
#everything is an object in python#
#    --------------------------------------

                # Numbers 
# integers = whole numbers / floats = decimals 

# convert other data types into float or integer using float() & int()
    # int("1") -> 1
    # float("1.1") -> 1.1
    # int(1.1) -> 1
#    --------------------------------------
             
               # Sequence Types
# Python has a number of different data types that store data
# the difference between them are the rules for organizing and accessing the data 

        #Lists 
# Any set of data that is separated by commas and enclosed in brackets is a list 
# Lists can also be created using the constructor. list() => [] 
# index based 
# essentially arrays from js
    # Functions for lists 
# len([1,3,4,5]) -> gives length of list  
# sorted([5,2,1,3]) -> sorts the list 
# .pop -> removes the last element in list 
# .remove(index) -> removes the element at that index 

        #Tuples 
# identical to lists except for two major differences: 
    # 1. no need for curly braces. only this -> tuple(1,2,3)
    # 2. tuples are immutable. once created, the tuple itself cannot be changed.
#           - methods like .pop() and .insert() cannot be used on tuples because they would change the contents on the tuple 



        #Sets and Dictionaries 
# Sequences data in python but the individual elements are unique 

    # Sets
# unindexed, unordered and unchangeable 
# initiated with set() class constructor 

# set() -> {}
# set(3,2,3,a,b,a) -> TypeError 
# set([3,2,3,a,b,a]) -> {2,3,a,b} 

# sets have many of the same methods as lists 
#   s = {1,2,3}
#   s.pop() -> 1
#   s.remove(3) -> {2}


    # Dictionaries 
# Python equivalent of JavaScript obj 
# Composed of Key/Value pairs 
# Create dictionaries by placing key value pairs inside curly brackets 
# Key value pairs must be in string format 
    # {"key1":"value1", "key2":"value2"}


# my_dict = { "key1": 1, "key2": 2 } 
# my_dict["key2"] -> 2
# Can access members of dictionary only using bracket notation 
# Create dictionaries using the dict() class constructor 
    # dict(x = 1, y = 2) -> {'x': 1, 'y': 2}


    # None
# represents the absence of any value 
# 









