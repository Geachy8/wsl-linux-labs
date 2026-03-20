import random
import string

print("🔐 Password Generator")

length = int(input("Enter password length: "))
use_symbols = input("Include symbols? (y/n): ").lower()

if length < 2:
    print("Password must be at least 2 characters long.")
    exit()

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Base characters
all_chars = letters + digits

if use_symbols == "y":
    all_chars += symbols

# Ensure at least one letter and one digit
password = [
    random.choice(letters),
    random.choice(digits)
]

# Fill the rest
for _ in range(length - 2):
    password.append(random.choice(all_chars))

# Shuffle to randomise order
random.shuffle(password)

# Convert to string
password = "".join(password)

print(f"\nGenerated password: {password}")
