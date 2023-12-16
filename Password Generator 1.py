import string
import random

#Getting password length
length = (input("Enter the password length :-"))
length = int(length)
print('''Choose character set for password from these:
      1. Digits
      2.Letters
      3.Special Characters
      4.Exit''')

characterlist = ""

#Getting character set for Password
while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):
        
        #Adding letters to possible characters
        characterlist += string.ascii_letters
    elif(choice == 2):
        
        #Adding digits to possible characters
        characterlist += string.digits
    elif(choice == 3):
        
        #Adding special characters to possible characters
        characterlist += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
        
password = []

for i in range(length):
    
    #pick a random character from our Characterlist
    randomchar = random.choice(characterlist)
    
    #appending a random character to password
    password.append(randomchar)
    
    #Printing password as a string
print("The random password is " + "".join(password))