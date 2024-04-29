# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"

# Creating a function
# Using a while loop
# Unilizing if/else statement

def solution(age):
    

    if age <= 13:
        return "drink toddy"
    elif age <= 17:
        return "drink coke"
    elif age <= 18:
        return "drink beer"
    elif age <=20:
        return "drink beer"
    elif age >=21:
        return "drink whisky"
    else:
        return "Enter a valid number."
    

    