#Create a program that ask the user to input their fullname. Print the input in all lower case.

def main():
    full_name = input("enter your full name: ")
    
    lowercase_name = full_name.lower()
    
    print("name in all lowercase letters:", lowercase_name)

if __name__ == "__main__":
    main()
