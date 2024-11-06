import random
import string

def password_generator(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    while True:

        length = int(input("\nEnter the length of the password: "))
        
        if length >= 6:
            password = password_generator(length)
            print("\nGenerated Password:", password)
            break
        
        else:
            print("\nInvalid input!!! TRY AGAIN...")

main()