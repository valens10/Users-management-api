import string, random


def generate_digits_code(length=6):
    key = ''.join(random.choices(string.digits, k=length))
    return key

