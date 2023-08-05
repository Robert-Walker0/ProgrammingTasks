import math

# Taken from a stackoverflow post.

def round(value):
    if math.ceil(value) - value <= 0.5: 
        return math.ceil(value)
    return math.floor(value)


# My own implementation of getting a number.
def get_input(prompt):
    try:
        value = int(input(prompt))
    except ValueError as InvalidInput:
        print(f"Error: {InvalidInput}")
        get_input()
    except EOFError:
        print("Ending the program.")
    else:
        return value
    