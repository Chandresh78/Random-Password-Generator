# For making a strong password, it should have combination of uppercase, lowercase, special characters.

# We will use random module
import random
chandreshlen = int(input("Please enter the length of the password to be generated: "))

chandresh = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*?"

password = "".join(random.sample(chandresh, chandreshlen))
print("Password has been generated: ", password)
