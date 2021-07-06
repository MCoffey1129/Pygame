
# Packages
import random
import numpy as np

print("Hello World")

# Assignment operators
x = 10
print(x) # value of 10

x = x+1
print(x) # value of 11

x+=1
print(x) # value of 12

# Using input code to interact with your code
# The inputs are assumed to be text unless we convert them to floats!!!
miles_driven_str = input("Enter miles driven:")
miles_driven = float(miles_driven_str)

gallons_used_str = input("Enter gallons used:")
gallons_used = float(gallons_used_str)

mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)

# Nest the above
miles_driven = float(input("Enter miles driven:"))


# if then else
a = 4
b = 5

if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")


# using and/or
if a > b and a == 10:
    print("a is greater than b")
elif a == b or b==4:
    print("a and b are equal")
else:
    print("b is greater than a")

# interacting with inputs
user_name = input("What is your name? ")
if user_name == "Martin":
    print("You have a nice name.")
else:
    print("Your name is ok.")

# Ensure that the response is case insensitive
user_name = input("What is your name? ")
if user_name.lower() == "martin":
    print("You have a nice name.")
else:
    print("Your name is ok.")


# Example 4: Ordering of statements
# Something with this is wrong. What?
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature > 100:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")


# Loops

for i in range(10):
    print("Hello")

# Nested loops
for i in range(4):
    print("Hello")
    for j in range(3):
        print("Martin")


# Keep a running total
total = 0
for i in range(5):
    score = float(input("score:"))
    total += score
    print("The total is:", total)

# Use a while loop to print the numbers 1 to 10 - do not use range function in a while loop
i=0
while i < 10:
    i +=1
    print(i)

# Looping until user wants to quit.
quit = "n"
while quit == "n":
    quit = input("Do you want to quit? ")

# Looping until the game is over or the user wants to quit
done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True

# Here is an example of using a while loop where the code repeats until the value gets close enough to one:
value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

# Random numbers
my_number = random.randrange(50)
print(my_number)

my_number = random.randrange(0,100)
print(my_number)

my_list = ['rock','paper','scissors']
print(my_list[random.randrange(3)])

# Floating point number between 0 and 1
random.random()

y = random.randrange(1,100)
print('I am thinking of a number between 1 and 100')
for i in range(7):
    x= int(input("Guess what number I am thinking of:"))
    if x > y:
        print("Too high!")
    elif x < y:
        print("Too low!")
    else:
        print("Great Work!")


# Computer graphics
#Importing and initializing Pygame
# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Defining colours
# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)


# Define Pi so we can draw arcs
PI = 3.1415926535

# Opening and setting the window size
# Open a window of width 700 pixels and height of 500
size = (700, 500)
screen = pygame.display.set_mode(size)
