#Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

def main():
    full_name = input("Please enter your full name with leading spaces: ")
    
    cleaned_name = full_name.lstrip()
    print("Your name without leading spaces is:", cleaned_name)

if __name__ == "__main__":
    main()