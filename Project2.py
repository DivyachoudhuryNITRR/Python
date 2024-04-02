#Random Password Generator

import random
import string #collection of string constants
# print(type(string.ascii_letters))
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)

# randNum=random.choice([1,2,3]) #can generate any random values from the list or any data structure 
# print(randNum)


pass_len=int(input("Enter the length of the password to generate : "))
charValues=string.ascii_letters+string.digits+string.punctuation


#List configuration [function for i in range(n)]
# password="".joint([random.choice(charValues) for i in range(pass_len)])

password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("Your random password is ",password)