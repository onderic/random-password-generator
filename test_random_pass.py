from random_pass import PasswordGenerator
import pytest


@pytest.fixture
def generator():
     #Create an object of the PasswordGenerator class with a length of 8
    return PasswordGenerator(8)

def test_password_generator(generator):
    # Generate a password and check if it has the correct length
    password = generator.generate_password()
    assert len(password) == 8


def test_password_wrong(generator):
    password = generator.generate_password()
    password2 = generator.generate_password()
    assert password != password2

def test_print_statement(capsys,generator):
    password  = generator.generate_password()
    print("Your random password is:", password)

    out, err = capsys.readouterr()
    assert out == f"Your random password is: {password}\n"