# Password Generator 
import random 
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '<', '>', '.', 
    '/', '?', '`', '~'
]

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
print("Welcome to Py Password Generator")
# 14
nr_number = int(input("How many numbers would you like in your password? "))
nr_letter = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))

password = ""
for ch in range(1, nr_number + 1):
    password += random.choice(number)
for ch in range(1, nr_letter + 1):
    password += random.choice(letters)
for ch in range(1, nr_symbols + 1):
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your generated password is: {password}")

