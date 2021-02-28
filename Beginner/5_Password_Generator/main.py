#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Example: 4 letter, 2 symbol, 2 number = g^2jk8&P

# List to store password
password = []

# Append a random letter from list of letters
for counter in range(1, nr_letters + 1):
  password.append(random.choice(letters))

# Appened a random symbol from list of symbols
for counter in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))

# Append a random number from list of symbols
for counter in range(1, nr_numbers + 1):
  password.append(random.choice(numbers))

# Shuffle the positions of the char in list password
random.shuffle(password)

# Loop through list and concat chars 
result = ""
for char in password:
  result += char

# Print the generated password
print(result)

