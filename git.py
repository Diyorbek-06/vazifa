# 1)   """NAME SHUFFER"""
# Write a function that returns a string in which firstname is swapped with last name.
# Example(Input --> Output)
# "john McClane" --> "McClane john"

# def name_shuffler(str_):
#     first, last = str_.split()
#     return f"{last} {first }"
# print(name_shuffler("john McClane"))


# 2) """Capitalization and Mutability"""
# Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.
# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. it must make the first character in the string upper case).
# The string will always start with a letter and will never be empty.
# Examples:
# "hello" --> "Hello"
# "Hello" --> "Hello" (the first letter was already capitalized)
# "a"     --> "A"

# def capitalize_word(word: str) -> str:
#     return word[0].upper() + word[1:]
# print(capitalize_word("hello"))
# print(capitalize_word("Hello"))
# print(capitalize_word("a"))


# 3) Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.
# Example:
# ['John', 'Smith'], 'Phoenix', 'Arizona'

# def say_hello(name, city, state):
#     full_name = " ".join(name)
#     return f" Welcome , {full_name}, to {city}, {state}!"
# print(say_hello(['john', 'Smith'], 'Phoenix', 'Arizona'))
# print(say_hello(["Jane ", ], "New York", "New York"))
# print(say_hello(["Alice", "Bob", "Xarter"], 'Austrin', "Texas"))

# 4) P. S. You can use \n in string to jump to the next line.
# Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about the format, look at the sample tests.

# def multi_table(number):
#     table = "\n".join([f"{i} * {number} = {i * number }" for i in range(1, 11)])
#     return table
# print(multi_table(5))

# 5) Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

# def remove_exclamation_marks(s):
#     return s.replace("!", '')
# print(remove_exclamation_marks("Hello world!"))
# print(remove_exclamation_marks("Python o'zgacha!!!"))
# print(remove_exclamation_marks("soz mavjud emas"))


# just for test

# second for test