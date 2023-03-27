#random password generator
import random

all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

length = int(input("Enter the desired length of the password: "))
password = ''.join(random.choice(all_chars) for i in range(length))

print("Your random password is:", password)