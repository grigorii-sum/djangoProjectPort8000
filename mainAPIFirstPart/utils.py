from random import choice
from string import ascii_letters, digits

'''
SIZE for making length of random code
AVAILABLE_CHARS for making set of available characters for random code
'''
SIZE = 7
AVAILABLE_CHARS = ascii_letters + digits


# Function for creating new random code of SIZE characters
def create_random_code(chars=AVAILABLE_CHARS):
    return "".join(choice(chars) for _ in range(SIZE))
