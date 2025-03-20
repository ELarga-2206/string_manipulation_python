#Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

def main():
    number = int(input("Please enter a number between 0 and 1000: "))
    
    six_digit_number = f"{number:06}"
    
    print("6-digit format is:", six_digit_number)

if __name__ == "__main__":
    main()