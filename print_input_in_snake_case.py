#Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

#get user input
#replace to snake case, use .replace
#must replace spaces with underscore
#replace capitals with lower cases

def to_snake_case(name):
    snake_case_name = name.lower().replace(" ", "_")
    return snake_case_name
