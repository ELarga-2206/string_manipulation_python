#Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#FUNCTION to_pascal_case(name):
# words = SPLIT name INTO INDIVIDUAL WORDS
# pascal_case_name = EMPTY STRING
# FOR each word IN words:
# capitalized_word = CAPITALIZE first letter of word
# pascal_case_name = pascal_case_name + capitalized_word

#pascal_case_name = CALL to_pascal_case(full_name)
# PRINT "Your name in PascalCase is:", pascal_case_name

def main():

    full_name = input("Please enter your full name in incorrect casing: ")
    pascal_case_name = to_pascal_case(full_name)
    
    print("Your name in PascalCase is:", pascal_case_name)

if __name__ == "__main__":
    main()

def to_pascal_case(name):

    words = name.split()
    pascal_case_name = ''.join(word.capitalize() for word in words)
    
    return pascal_case_name