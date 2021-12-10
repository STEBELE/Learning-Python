import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B'
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_letters = ""
password_symbols = ""
password_numbers = ""
for i in range(1, nr_letters+1):
    password_letters += letters[random.randint(1, len(letters)-1)]
for i in range(1, nr_symbols+1):
    password_symbols += symbols[random.randint(1, len(symbols)-1)]
for i in range(1, nr_numbers+1):
    password_numbers += numbers[random.randint(1, len(numbers)-1)]

# print(password_letters)
# print(password_symbols)
# print(password_numbers)
lenght_password = nr_letters + nr_symbols + nr_numbers
passcode = password_letters + password_symbols + password_numbers
password = ""
print(passcode)
for i in range(1,lenght_password +1):
    password += passcode[random.randint(1, len(passcode)-1)]

# for char in range(1,lenght_password +1): rFfW*#6688
    
# print(password)
