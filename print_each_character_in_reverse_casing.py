#Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

#FUNCTION reverse_case(char):
#IF char is lowercase:
#RETURN uppercase version of char
#ELSE IF char is uppercase:
#RETURN lowercase version of char
#ELSE: RETURN char (leave unchanged)

#FOR each character in full_name:
        #reversed_char = CALL reverse_case(character)
        #reversed_case_name = reversed_case_name + reversed_char

    #PRINT "Your name with reversed casing is lmao:", reversed_case_name smth

#CALL main()

def reverse_case(char):
    if char.islower():
        return char.upper()
    if char.isupper():
        return char.lower()
    else:
        return char
    
def main():
    full_name = input("Please enter a name in incorrect casing: ")
    
    reversed_case_name = ''.join([reverse_case(char) for char in full_name])
    
    print("reversed case:", reversed_case_name)

if __name__ == "__main__":
    main()