#Create a program that ask the user to input a complete statement. Print the number of words in the input.

def main():
    statement = input("Please enter your statement: ")

    num_words = len(statement.split())

    print("number of words is: ", num_words)

if __name__ == "__main__":
    main()