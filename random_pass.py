import string
import random


class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate_password(self):
        # Generate a random string of lowercase letters, uppercase letters, and digits
        password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase
        + string.digits, k= self.length))
        return password     

# Create an object of the PasswordGenerator class
gen = PasswordGenerator(8)

# Generate and print the password
password = gen.generate_password()
print("Your random password is:",password)
