#Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

def to_snake_case(name):
    snake_case_name = name.lower().replace(" ", "_")
    return snake_case_name

def main():
    full_name = input("Please enter your full name in incorrect casing: ")
    
    snake_case_name = to_snake_case(full_name)
    print("Your name in snake_case is:", snake_case_name)

if __name__ == "__main__":
    main()