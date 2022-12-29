# Password Generator

This is a simple Python class that generates random passwords of a specified length.

## Installation

To use this class, you will need to have Python 3 and the `random` and `string` modules installed. These modules are part of the Python standard library and should be included with your Python installation.

## Usage

To use the `PasswordGenerator` class, you can create an object of the class and call the `generate_password` method on it:

```python
from password_generator import PasswordGenerator

# Create an object of the PasswordGenerator class with a length of 8
generator = PasswordGenerator(8)

# Generate and print a password
password = generator.generate_password()
print(password)


The generate_password method generates a random password using a combination of lowercase letters, uppercase letters, and digits, and returns it as a string.

Tests
To run the tests for this class, you will need to have the pytest module installed. You can install pytest using pip:

Copy code
 pip install pytest
Once pytest is installed, you can run the tests using the pytest command:

Copy code
 pytest test_password_generator.py
This will run the test functions and report the results.

License
 This project is licensed under the MIT License. See the LICENSE file for details.

I hope this helps! Let me know if you have any questions.
