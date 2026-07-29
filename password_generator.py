import random
import string

print("========== Password Generator ==========")

#  Take the length of the password from user
length = int(input("Enter the password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

# Empty password
password = ""

# Generate password
for i in range(length):
    password += random.choice(characters)

# Display the Password
print("\nGenerated Password:", password)