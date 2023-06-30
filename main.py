import secrets
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
special_characters = string.punctuation

password = []

password.append(secrets.choice(uppercase_letters))
password.append(secrets.choice(lowercase_letters))
password.append(secrets.choice(numbers))
password.append(secrets.choice(special_characters))

length = int(input('\nEnter the length of password: '))

character_set = uppercase_letters + lowercase_letters + numbers + special_characters
for _ in range(length - 4):
    password.append(secrets.choice(character_set))

secrets.SystemRandom().shuffle(password)

generated_password = ''.join(password)

print("Your password is ", generated_password)