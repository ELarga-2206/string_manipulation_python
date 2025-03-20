#Create a program that ask the user to input their fullname. Print the number of characters in the input.

def main():
    
    full_name = input("Please enter your name: ")

    num_characters = len(full_name.replace(" ", ""))
    print("no. of characters in your name:", num_characters)

if __name__ == "__main__":
    main()