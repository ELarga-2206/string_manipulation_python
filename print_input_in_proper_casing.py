#Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

def to_proper_case(name):
    proper_case_name = name.title()
    return proper_case_name

def main():
    full_name = input("Please enter your full name in incorrect casing: ")
    proper_case_name = to_proper_case(full_name)
    print("Your name in proper casing is:", proper_case_name)

if __name__ == "__main__":
    main()