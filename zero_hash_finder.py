# Michael Ferrie - Sep, 2019

# Write a program that will keep adding a random character to the enhttps://github.com/michaelferrie/python_hashing/blob/master/zero_hash_finder_gui.pyd of
# the input_string until the output_hash starts with 4 zeros
# the program should print out the new input_string each time until the
# desired md5hash is discovered
# If the input string is changed the program should still work

import hashlib
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?-+=@#&*"
random_char = random.choice(chars)
input_string = "Hello World"
new_guess = input_string + random.choice(chars)
first_four = new_guess[:1]


while first_four[:5] != ("00000"):
    new_guess += random.choice(chars)
    result = hashlib.md5(new_guess.encode()) 
    output_hash = (result.hexdigest())
    first_four = (output_hash)[:5]
    print (new_guess)
    print (output_hash)
