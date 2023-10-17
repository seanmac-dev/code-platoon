# zip
numbers = [1, 2, 3]
letters = ["a", "b", "c"]

# zipped = zip(letters, numbers)
# print(list(zipped))
zipped_dic = dict(zip(letters, numbers))
print(zipped_dic)
# user_input = input("Please enter your favorite language")

# upper = user_input.upper()
# print(upper)

# match upper:
#     case "PYTHON":
#         print("Mine too!")

# import functools

# print("hello")
# print("jonathan".capitalize())

# name = "Alice"
# print(f"Hello, my name is {name}")

# berries = ["raspberry", "blueberry", "strawberry", "blackberry"]
# print(berries[0])
# # can access items in list by index

# print(berries[1:3])
# # can slice with start point and excludes end point
# # ['blueberry', 'strawberry']

# print(berries[:3])
# # slice everything up to but not including blackberry

# print(berries[::-1])
# # reverse list

# # TUPLE
# # kinda like a list, but immutable

# days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print(days_of_the_week[4])
# # if single element in tuple, you must include the comma after like this (1,) so python knows it's a tuple.

# day = days_of_the_week + ("Saturday",)
# print(day)


# t = (0, 1, 2)
# t_add = t + (3, 4, 5)
# print(t_add)

# # DICTIONARIES

# jeff = {
#     "name": "jeff",
#     "age": 45,
#     "job": "influencer",
# }

# print(jeff["age"])
# print(jeff.get("age"))
# print(jeff.keys())
# print(jeff.values())
# print(jeff.items())

# jeff["education"] = "college"
# print(jeff)

# if "job" in jeff:
#     print("Yep, it's in there.")


# #  FUNCTIONS
# def gimme_five():
#     return 5


# print(gimme_five() + 10)


# def add_one(n):
#     return n + 1


# def describe_berries(n, color):
#     print(f"I have {n} {color} berries.")


# # order of arguments does matter


# # print as many args as you want
# def print_them_all(*args):
#     print(args)

#     print_them_all("alice", "bob", "carol")


# # keyword args are named arguments
# # you can also use this to set a default value
# def describe_berries(n=1, color="blue"):
#     print(f"I have {n} {color}berries")


# # with keyword args, arguments orders does not matter
# describe_berries(color="rasp", n=3)


# def who_am_i(**kwargs):
#     for k in kwargs:
#         print(f"My {k} is {kwargs[k]}")


# who_am_i(name="dan", age="20")

# # IF STATEMENTS & LOOPS


# def can_drink_beer(age, country):
#     if age >= 21 or age >= 18 and country == "Canada":
#         return True
#     elif country == "Antarctica":
#         return True
#     else:
#         return False


# print(can_drink_beer(17, "Canada"))

# # looping
# my_list = ["a", "b", "c"]
# for char in my_list:
#     print(char)

# # range includes start to finish, inclusive (0, 10)
# one_to_ten = range(10)
# print(one_to_ten)

# # loop through range
# for x in one_to_ten:
#     print(x)

# # loop thru list and get an index
# for index, el in enumerate(one_to_ten):
#     print(index, el)

# # loop through ranges
# for index, el in enumerate(my_list):
#     print(index, el)

# # can loop thru dict
# my_dict = {"donuts": "yummy", "green beans": "gross"}

# for key in my_dict:
#     print(my_dict[key])

# for value in my_dict.values():
#     print(value)

# # While loops
# x = 9
# while x > 0:
#     print(x)
#     x -= 1

# # Built in methods because everything is an object
# # capitalize method
# print("jonathan".capitalize())
# first_name = "jonathan"
# first_name.capitalize()

# # Replace built in method
# print("young".replace("g", "12345"))

# # different way to do it
# last_name = "young"
# print(last_name.replace("y", "456"))

# # Reduce method
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = functools.reduce(lambda agg, item: agg + item, my_list)
# print(sum)
# # 55

# # Sort method
# people = [
#     {
#         "name": "alice",
#         "age": 44,
#         "job": "influencer",
#     },
#     {
#         "name": "bob",
#         "age": 49,
#         "job": "dog walker",
#     },
#     {
#         "name": "carol",
#         "age": 35,
#         "job": "life coach",
#     },
# ]
# # This sorts the original list
# people.sort(key=lambda k: k["age"])

# # key is a 1-argument function that describes how to sort the list.
# # This returns a new list (original list is not modified)
# # This example sorts by age
# people_sorted = sorted(people, key=lambda k: k["age"], reverse=True)
# print(people_sorted)

# # reversed
# people.reverse()
# print(list(reversed(people)))


# # you can also loop thru dictionaries
# another_dict = {"green beans": "gross", "donuts": "yummy"}

# if "donuts" in another_dict.keys():
#     print("we have donuts")

# if "yummy" in another_dict.values():
#     print("Yummmmmyyyy")

# # switch case
# lang = input("What's the programming language you want to learn? ")

# match lang:
#     case "Javascript":
#         print("You can become a web developer.")

#     case "Python":
#         print("You can become a data scientist.")

#     case "Solidity":
#         print("You can become a Blockchain developer.")

#     case _:
#         print("It does not matter. What matters is to get hands on coding")


# # Lamda functions
# ## typical function example
# def add_one(x):
#     return x + 1


# print(add_one(7))  # output would be 8


# # First-class function
# def say_hello(name):
#     print(f"hello {name}")


# def say_hello_extra(name, other_hello_function):
#     print(f"hi {name}")
#     other_hello_function(name)


# say_hello_extra("Alice", say_hello)


# ## lambda function example
# def add_one(x):
#     return x + 1


# add_two = lambda x: x + 2

# print(add_two(7))  # output would be 9

# say_hi = lambda name: f"hello {name}"

# say_hello_extra("Bob", say_hi)

# # map function
# # take each item in list and do this to that item
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = map(lambda item: item + 2, my_list)
# print(list(new_list))

# # filter function
# # take each item, if it's divisible by 3, add to new list
# new_list_divisible_by_three = filter(lambda item: item % 3 == 0, my_list)
# print(list(new_list_divisible_by_three))

# # reduce
# # takes each item in the list and adds to previous one, storing each value collectively in agg
# a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sum = functools.reduce(lambda agg, item: agg + item, a_list)

# print(sum)

# to_do_list = []

# input_string = input("Enter elements separated by space \n'")
# user_list = input_string.split()
# print(type(user_list))


# len(to_do_list) == 0
# to_do_list.append("yesss")


# # user_input = input("What would you like?")
# # print(user_input)

# tasks = {}

# user_input = input("Please enter a key")
# print(user_input)

# tasks[user_input] = user_input
# print(tasks)
