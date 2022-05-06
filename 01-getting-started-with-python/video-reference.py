# This is marked out code.
'''
Docstrings allow us to to create text that spans multiple lines. 
'''

# Key Terms
'''
Console 
  - Screen where outputs are displayed
Output
  - Displayed text in console
Syntax
  - Structure that indicates to python to perform certain functions
Print
  - Function that populates console with data
Return
  - Assigns a value to a certain reference/location
'''

# Data Types
'''
• Objects (Objects Diagram)
  - strings
  - integers
  - variables
  - booleans True or False
  - None
  - etc...

strings: Text
  Ex: 'This is text. It is not intended to tell the computer to do anything'
  Syntax: '' or ""

integer: Number
  Ex: 100000000000
      -359479875938759843

boolean (bool): True or False
Is it night time where I'm at?
boolean => False
Is it day time where I'm at
boolean => True

null: None
syntax: None
'''

# Variable Assignment
'''
Purpose: assign value to an object
Syntax: =
Ex: some_variable = "Test"
==: Is equal to
'''

# Print Statement
'''
Syntax: print(some_variable)
'''
print("Hello World")
print(2 + 2)

# Examples
first_cat_name = "Pepper"
print(first_cat_name)
first_cat_age = 4
print(first_cat_age)
print("My first cat's name is ", first_cat_name)

# fstring (format string)
print(f"My first cat's name is {first_cat_name} and his age is {first_cat_age}")

# Inputs
'''
Syntax: input()
'''
second_cat_name = input("What is your second cat's name?")
print(second_cat_name)
second_cat_age = input("How many months is she?")
print(type(second_cat_age))
print(type(4))


#Operators
'''
+ Addition
- Subtraction
* Multiplication
/ Division
** Exponentials
'''
print(2 + 2)
print(2 - 10)
print(2 * 5)
print(2 ** 10)
print(10 / 2)
calculated_variable = 2 * 2
print(f"This is our calculated variable {calculated_variable}")


#Equality evaluators
'''
x == y means that x is equal to y
x > y means that x is greater than y
x >= y means that x is greater than, or equal to, y
x < y means x is less than y
x <= y means x is less than, or equal to, y
Returns a boolean
'''
x = 10
y = 50
print(x == y)
print(x < y)
print(x <= y)


#Data Structures
'''
List
Syntax: [] or list()
'''
  #Example
cats = [first_cat_name, "Peach"]
print(cats[1])

'''
Dictionary 
Syntax: {} or dict()
Purpose: Create key, value pairs in an ordered object
'''
  #Example
#family = {}
#family = dict()
family = {
  "Mom": '',
  "Dad": "",
  "Daughter": "Julia",
  "Son": "Oscar"
}

family["Mom"] = "Stephanie"
family["Dad"] = "Tony"
family["Pets"] = cats

print(family)

'''
Tuple
Syntax = ()
'''
  #Example
#cats_tuple = ()
cats_tuple = ("Pepper", "Peach")
print(cats_tuple)


#Conditionals
'''
- if 
- - syntax: if conditional:
- - purpose: Checks if conditional is True

- else if 
- - syntax: elif conditional:
- - purpose: Checks if conditional is True if previous conditionals are false

- else
- - syntax: else
- - purpose: Tells the program what to do if none of the if/elif statements are True
'''
if ("Mom" in family): #True
  print(f"Mom's name is {family['Mom']}")
  
if ("Dad" in family): #True
  print(f"Dad's name is {family['Dad']}")
  
if "Cousin" in family: #False
  print(f"Cousin's name is {family['Cousin']}")
elif "Omar" in family: #False
  print(f"Cousin's name is {family['Omar']}")
else:
  family["Cousin"] = "Omar"

print(family)


# Loops
'''
• Key-terms: iterable, iteration, range
• Purpose: iterate over an  iterable for a given range.
• for loop
  - Syntax: for iteration in iterable:
• while loop
  - Syntax: while iteration in range(iterable):
'''
  # Examples
food_choices = ["Paella", "California Rolls", "Gyro", "BBQ Pizza", "Double Cheeseburger"]
user_choice = input("What food would you like")
print(user_choice)

for choice in food_choices:
  if choice == user_choice:
    print(f"This item is on our list. You have selected: {choice}")

california_rolls = 12
while (california_rolls > 0):
  california_rolls -= 1 #Eat california roll
  print(f"You have {california_rolls} rolls left")