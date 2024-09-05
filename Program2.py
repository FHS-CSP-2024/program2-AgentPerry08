# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
name = input("Yo! Please tell me your name! \n ")
print("Hi " + name )
print("Hi " + name )




## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
name = input("Hola! Please tell me your name! \n")
print ("!" + name + " "+ "!"+ name)


## Problem 3 ##
#Please write a script that: 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
firstname = input("What is your first name? \n")
lastname = input("What is your last name? \n")
address = input("What is your street address? \n")
cityandpost = input("What is your city and postal code? \n")

print("\n Here are your details:")
print("First name: " + firstname)
print("Last name: " + lastname)
print("Street address: " + address)
print("City and postal code: " + cityandpost)

## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
word1 = input("Please tell me the first word: \n")
word2 = input("What is the second word: \n")
word3 = input("What is the third word: \n")

print(word1 + "-" + word2 + "-" + word3)

## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.
name = input("Enter the name: \n")
year = input("Enter the year: \n")

print("\n")
print("In " + year + ", Commander " + name + " faced a code red: a dragon attack.")
print(name + " swiftly organized the defense, leading the charge.")
print("The mission was clear: protect the base, eliminate the threat.")
