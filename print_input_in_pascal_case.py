#Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

def to_pascal_case(name):
    words = name.split()
    
    pascal_case_name = ''.join(word.capitalize() for word in words)
    
    return pascal_case_name

def main():
    full_name = input("enter your full name in random casing: ")
    
    pascal_case_name = to_pascal_case(full_name)
    
    print("PascalCase:", pascal_case_name)

if __name__ == "__main__":
    main()