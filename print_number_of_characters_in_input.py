#Create a program that ask the user to input their fullname. Print the number of characters in the input.

#FUNCTION main():
# PRINT "Please enter your full name:"
# full_name = GET user input
# num_characters = CALCULATE LENGTH OF full_name
# PRINT "The number of characters in your name is:", num_characters

#initial code idea, reused since its similar to others
def main():
    # Ask the user to input their full name in incorrect casing
    full_name = input("Please enter your full name in incorrect casing: ")
    
    # Convert the input to snake_case
    snake_case_name = to_snake_case(full_name)
    
    # Print the result
    print("Your name in snake_case is:", snake_case_name)

if __name__ == "__main__":
    main()