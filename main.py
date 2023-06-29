import random
import string

length = int(input('\nEnter the length of password: '))

all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = "".join(random.sample(all, length))
print(password)