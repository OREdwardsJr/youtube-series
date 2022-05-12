"""
• Instructions:
You are meeting with your friend, Amy, to have dinner with her family. Below is a story that talks about
your experience at dinner. Fill in the variables below so that the story makes sense. Feel free to make up
the family names as you please.

The format is at such:

#Enter code below

#Enter code above

You are expected to enter your code between "#Enter code below" and "#Enter code above". For example it should look like the following:
#Enter code below

variable = "Test
print(variable)

#Enter code above


•Testing your answers:
When you have created all of the variables then run your program. If no errors occur, and you can choose a food within the options,
then your progam functions as expected!

Troubleshooting:
If you run into difficulties then you can reference "exercise answer.py" for an example.
"""

'''
---------------- Begin Exercise ----------------
'''

# Variable Assignment
"""
• Create a variable called "cat" and assign it with a name.
• Crate a variable called "dog" and assign it with a name.
• Create a variable called "servings" and assign it an integer for the amount of servings you want to eat.
"""
# Enter code below

# Enter code above


# List Creation
"""
• Create a list called "pets". Fill the list with variables cat and dog.
• Create a list called "food_choices". Fill it with 4 food options for dinner.
"""
# Enter code below

# Enter code above


# Dictionary Creation
"""
• Create a dictionary called "family". The dictionary should consist of a family with keys: "Mom", "Dad", "Friend", "Brother", and "Pets".
The value for "Friend" should be "Amy". The value for the key "Pets" should be the pets list created above.
"""
# Enter code below

# Enter code above


# Conditionals
"""
• Create an if/elif/else statement that checks whether "Cousin" is a key in your family dictionary. 
    - If it exists then print "Cousin exists in the family".
    - If it is not, check if "Omar" exists in the family.
        - If it exists then print "Omar is in the family"
    - If neither are true then create a key named "Cousin" and provide it with a name for the value pair in your family dictionary.
"""
# Enter code below

# Enter code above


# Inputs
"""
• Create a variable called "my_choice" and assign it an input statement. 
    - The input should ask "What dish would you like?" and your input should match a dish in food_choices.
• Create a variable called "servings" and assign an input statement to it. 
    - The input should ask "How many servings would you like?"
"""
# Enter code below

# Enter code above


# For Loop
"""
• Create a for loop that iterates through each item in the list food_choices.
    - If your variable my_choice matches an item in food_choices then assign the boolean True to a variable named "success".
• Enter your code for the for loop below underneath the hashtag "#Create for loop".
"""
# Create for loop
def choose_food():  # This is a function. Do not worry too much about what this does yet.
    success = False
    # Enter code below - Don't edit above.

    # Enter code above - Don't edit below.
    if success:
        return "'Sure I can make that!'"
    else:
        return "'That's not in the list but I'll try to make it'"


# While loop
"""
• Create a while loop that subtracts from servings until you've eaten it all (EG: servings > 0). 
    - As a reminder, use -= to subtract from a variable while assigning your variable the new value.
        - EG: some_variable -= 1
"""
# Create while loop
def eat_food(serving):
    # Enter code below - Don't edit code above.

    # Enter code above - Don't edit code below.
    if serving == 0:
        return "Good job you ate all of your food!"
    else:
        return f"You still have {serving} left! Was the food not good? Try editing your while loop again!"
        


'''DO NOT EDIT BELOW'''
story = f"""
I had dinner with Amy tonight! I was very excited, especially to meet {pets}! Her cat name is {cat} and her dog name is {dog}.
Her family is made up of {family}. Her mother, {family["Mom"]} offered to make any of the following dishes: {food_choices}. 
I decided to eat {servings} servings of {my_choice}. Her response when I asked for {my_choice} was {choose_food()}. After I ate,
she looked at me and said '{eat_food(int(servings))}'.
"""

print(story)
