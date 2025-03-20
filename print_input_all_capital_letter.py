#Create a program that ask the user to input their fullname. Print the input in all capital letter.

def main():
    full_name = input("enter full name: ")
    
    capitalized_name = full_name.upper()
    
    print("name in all capital letters:", capitalized_name)

if __name__ == "__main__":
    main()