#Create a program that ask the user to input a complete statement. Print the number of words in the input.

#FUNCTION main():
# PRINT "Please enter a complete statement:"
# statement = GET user input
# words = SPLIT statement INTO A LIST OF WORDS
# num_words = COUNT THE NUMBER OF WORDS IN THE LIST
# PRINT "The number of words in your statement is:", num_words

def main():
    statement = input("Please enter your statement: ")

    num_words = len(statement.split())

    print("number of words is: ", num_words)

if __name__ == "__main__":
    main()
