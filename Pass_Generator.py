import random, string
import sys
import pyperclip

print("-" * 50)
print(" ")
print("\t\tPassword Generator by @var-log")
print(" ")
print("-" * 50)

char_size = 1
password = ""

while char_size:
    char_size = int(input("How many chars do you want in your password? Choose between 4 and 21: "))
    if 4 <= char_size <= 21:
        print("\nHere's your new Password: ")
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(char_size))
        print(" ")
        print(password)
        print(" ")
        pyperclip.copy(password)
        print("Already copied to clipboard, green light to use it!")
        sys.exit(1)
    else:
        print("Please choose a number within the range. 4-21")
    continue
