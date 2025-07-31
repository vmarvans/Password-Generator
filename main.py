import random
import string

def main():
    print("Welcome to the Password Generator!")
    length = get_length()
    types = get_types()
    print(generate_password(length, types))
def get_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Password length must be at least 1 character.")
                return get_length()
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def get_types():
   options = {
        'letters': "Include letters? (y/n): ",
        'digits': "Include digits? (y/n): ",
        'special characters': "Include special characters? (y/n): "
    }
   
   types = [key for key, prompt in options.items() if input(prompt).lower() == 'y']

   if not types:
        print("You must select at least one character type.")
        return get_types()
    
   return types
    
   
def generate_password(length, types):

    characters = ''
    if 'letters' in types:
        characters += string.ascii_letters
    if 'digits' in types:
        characters += string.digits
    if 'special characters' in types:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    
    
if __name__ == "__main__":
    main()


