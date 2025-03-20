#Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

#how to change into proper casing?

#FUNCTION to_proper_case(name):
# proper_case_name = CONVERT name TO PROPER CASING (first letter of each word capitalized, rest lowercase)
# RETURN proper_case_name
# FUNCTION main():
# PRINT "Please enter your full name in incorrect casing:"
# full_name = GET user input
#print proper_case_name

def to_proper_case(name):
    proper_case_name = name.title()
    return proper_case_name

def main():
    full_name = input("Please enter your full name in incorrect casing: ")