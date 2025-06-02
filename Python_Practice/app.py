# print("Sukhbir Singh Ghotra")
# print('o----')
# print(' ||||')
# print('*' * 10)
from email.policy import EmailPolicy
from platform import processor
from sys import dont_write_bytecode

#################################################

# price = 10
# rating = 4.9
# name = 'Sukhbir'
# is_published = True
# print(price)

#################################################

# full_name = 'John Smith'
# age = 20
# is_new = True

#################################################

# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(name + ' like ' + color)

#################################################

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2025 - int(birth_year)
# print(type(age))
# print(age)

#################################################

# weight = input('What is your weight(lbs): ')
# weight = float(weight) * 0.453592
# print("Your weight(kgs): " + str(weight))

#################################################

# course = 'Python for "Beginners"'
# print(course)

#################################################

# course = '''
# Hi John,
#
# Here is our first email to you.
#
# Thank you,
# The Support Team
#
# '''
# print(course)

#################################################

# course = 'Python for Beginners'
# another = course[:]
#
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:5])
# print(course[:])
# print(another)

#################################################

# name = 'Jennifer'
# print(name[1:-1])

#################################################

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

#################################################

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)
#
# print(course.find('P'))
# print(course.find('o'))
# print(course.find('O'))
# print(course.find('Beginners'))
# print(course.replace('beginners', 'Absolute Beginners'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course.replace('P', 'J'))
# print('Python' in course)
# print('python' in course)
#
# len()
# course.upper()
# course.lower()
# course.title()
# course.find()
# course.replace()
# '...' in course

#################################################

#Arithmatics
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)   # floor divion
# print(10 % 3)    # modulus
# print( 10 ** 3)  # power / exponent
#
# x = 10
# x = x + 3
# x += 3
# print(x)

# operators precedence

# exponentiation 2 ** 3
# multiplication or division
# addition or subtraction
# we can use parenthesis to change the order of operators precedence

# x = 10 + 3 * 2
# print(x)
#
# x = 10 + 3 * 2 ** 2
# print(x)

# x = (10 + 3) * 2 ** 2
# print(x)

# x = (2 + 3) * 10 - 3
# print(x)

# import math
#
#
# x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(math.ceil(2.9))
# print(math.floor(2.9))

#################################################

# if conditions

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")

#################################################

# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

#################################################

# Logical Operators

# has_high_income = False
# has_good_credit = True
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

#################################################

# Comparison Operators

# temperature = 35
#
# if temperature != 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# Example program

# name = input("Enter your name: ")
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")

#################################################
# Project: Weight converter

# weight = int(input("Weight: "))
# conversion = input("(L)bs or (K)g: ")
# if conversion.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} Kgs")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} Lbs")

#################################################
# While Loops

# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")

# Guessing Game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print("Sorry, you failed!")

#################################################
# Car Game

# command = ""
# started = False
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that.")

#################################################

# For Loops

# for item in 'Python':
#     print(item)

# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)

# for item in [1, 2, 3, 4]:
#     print(item)

# for item in range(10):
#     print(item)

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
#
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

#################################################

# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)

# for x in range(4):
#     print(x)

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# For loop project
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[2:])
# print(names)

# name = ''
# for x in names:
#     if len(x) > len(name):
#         name = x
# print(name)

# Find largest number in list
# numbers = [3, 6, 2, 8, 4, 10]
# largest_num = numbers[0]
# for num in numbers:
#     if num > largest_num:
#         largest_num = num
# print(largest_num)

#################################################
# 2d

# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 20
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)

#################################################

# List functions

# numbers = [5, 2, 1, 5, 7, 4]
# numbers.append(20)
# numbers.insert(0, 10)
# print(numbers.index(50))
# print(50 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers.sort())
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)

# Remove duplicate from list
# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

#################################################
# Tuples

# numbers = (1, 2, 3)
# numbers[0] = 10
# print(numbers[0])


#################################################
# Unpacking
# coordinates = (1, 2, 3)
# # coordinates[0] * coordinates[1] * coordinates[2]
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
#
# x, y, z = coordinates
# print(x)
# print(y)

# coordinates = [1, 2, 3]
# x, y, z = coordinates
# print(x)
# print(y)

#################################################
# Dictionaries

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# customer["name"] = "Jack Smith"
# print(customer["name"])
# customer["birthdate"] = "Jan 1 1980"
# print(customer["birthdate"])
# print(customer.get("birthdate", "Jan 1, 1980"))

# Exercise
# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# Emoji Converter

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "😒"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

#################################################

# Functions
# Parameters: variable names > i.e greet_user(first_name, last_name)
# Positional Arguments: value of the variables are being passed when calling the function. i.e greet_user("Smith", "John")
# keywords Arguments: when calling the functions; values are named and the order of the arguments do not matter for the parameters. i.e greet_user(last_name="Smith", first_name="John")
# Note: when calling function with arguments, user positional arguments first and then use keywords arguments. i.e greet_user("Smith", first_name="John")
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user(last_name="Smith", first_name="John")
# print("Finish")

#################################################

# Return Statement

# def square(number):
#     print(number * number)
#     return None
#
# print(square(3))

#################################################

# def emoji_converter(message):
#
#     words = message.split(' ')
#     emojis = {
#         ":)": "😊",
#         ":(": "😒"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))

#################################################

# Exceptions
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

#################################################

# Comments
# print sky is blue
# print("Sky is blue")

#################################################

# Classes

# Numbers
# Strings
# Booleans
# -------
# Lists
# Dictionaries

# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)

#################################################

# Constructors

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)


# ######### Exercise

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# john = Person("John Smith")
# john.talk()
#
# bob = Person("Bob Smith")
# bob.talk()

#################################################

# Inheritance

# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
#
# cat1 = Cat()
# cat1.walk()
#
# dog1 = Dog()
# dog1.walk()


#################################################

# Modules
# import converters
# from converters import kg_to_lbs
#
# kg_to_lbs(100)
#
# print(converters.kg_to_lbs(70))

# Exercise

# import utils
#
# numbers = [10, 3, 6, 2]
#
# max_number = utils.find_max(numbers)
# print(max_number)

#################################################

# Packages

#import ecommerce.shipping
#from ecommerce.shipping import calc_shipping
# from ecommerce import shipping
# shipping.calc_shipping()

#################################################

# Generating Random Values

# Python 3 module index  -- google it to see all the module

# import random

# for i in range(3):
#     # print(random.random())
#     print(random.randint(10, 20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())


#################################################

# from pathlib import Path

# Absolute path
# Relative path

# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

# path = Path()
# print(path.glob('*.py'))
# for file in path.glob('*.py'):
#     print(file)

#################################################

# Pypi and Pip

# Excel Spreadsheets

# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#               min_row=2,
#               max_row=sheet.max_row,
#               min_col=4,
#               max_col=4)
#
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#
#     wb.save(filename)

#################################################

# Machine Learning

# Libraries and Tools
# Numpy, Pandas, MatPlotLib, Scikit-Learn
# Jupyter, Anaconda

# Import a Data Set

























#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################

























