import random

password_chars = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
letters_password = int(input("How many letters would you like in your password? "))
simbol_password = int(input(f"How many symbols would you like? "))
nums_password =  int(input(f"How many numbers would you like? "))


# Generate the elements

for char in range(1, letters_password + 1):
  password_chars.append(random.choice(letters))

for char in range(1, simbol_password + 1):
  password_chars.append(random.choice(symbols))

for char in range(1, nums_password + 1):
  password_chars.append(random.choice(numbers))

random.shuffle(password_chars)

password = ""
for char in password_chars:
  password += char

print(f"Your password is: {password}")
