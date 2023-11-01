from bisect import bisect_left

"""Recursion practice"""
# def countdown(n):

#     if n != 1:
#         countdown(n - 1)
#     print(n)


# countdown(10)

"""Linear search"""
# O(n) linear search time complexity grows linearly as n grows
# if you have 100 items in a list, it takes 100 steps
# When to use: consider using when data is not sorted

# def linear_search(a_list, n):
#     for i in a_list:
#         if i == n:
#             return True
#     return False


# a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
# print(linear_search(a_list, 91))

"""Linear search using python's built-in 'in' keyword"""
# unsorted_list = [1, 45, 4, 32, 3]
# print(45 in unsorted_list)

"""Binary search"""
# O(log n)
# When to use: to drastically reduce search scope (cutting in half each iteration)
# Data needs to be sorted, but if unsorted, need to weight if it's worth sorting.

# def binary_search(a_list, n):
#     first = 0
#     last = len(a_list) - 1

#     while last >= first:
#         mid = (first + last) // 2
#         if a_list[mid] == n:
#             return True
#         else:
#             if n < a_list[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return False


# print(binary_search([1, 4, 98, 357, 9203], 9203))

"""Binary Search built-in keyword 'bisect-left'"""
# from bisect import bisect_left


# sorted_fruits = ["apple", "banana", "orange", "plum"]
# print(bisect_left(sorted_fruits, "banana"))
# prints index of banana: 1
# will also return where an item would go if it were in your iterable
# "kiwi" would go in index 2, but to check we have to do the below:


# def binary_search(an_iterable, target):
#     index = bisect_left(an_iterable, target)
#     if index <= len(an_iterable) and an_iterable[index] == target:
#         return True
#     return False


# print(binary_search(["a", "c", "e", "p"], "e"))

"""Practice challenge binary search"""
# Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list.


# def binary_search(an_iterable, target):
#     index = bisect_left(an_iterable, target)
#     if index <= len(an_iterable) and an_iterable[index] == target:
#         return True
#     return False


# print(binary_search(["apple", "banana", "cucumber", "date"], "cucumber"))

"""Bubble sort"""
# O(n^2) because it relies on two nested for loops

# def bubble_sort(a_list):
#     list_length = len(a_list) - 1
#     for i in range(list_length):
#         no_swaps = True
#         for j in range(list_length - i):
#             if a_list[j] > a_list[j + 1]:
#                 a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
#                 no_swaps = False
#         if no_swaps:
#             return a_list
#     return a_list


# print(bubble_sort([32, 56, 8, 3, 46, 1]))

"""Arrays"""
# def move_zeros(a_list):
#     zero_index = 0
#     for index, n in enumerate(a_list):
#         if n != 0:
#             a_list[zero_index] = n
#             if zero_index != index:
#                 a_list[index] = 0
#             zero_index += 1
#     return a_list


# a_list = [8, 0, 3, 0, 12]
# move_zeros(a_list)
# print(a_list)

"""Combine List"""
# movie_list = ["Interstellar", "Inception", "The Prestige", "Insomnia", "Batman Begins"]

# ratings_list = [1, 10, 10, 8, 6]

# print(list(zip(movie_list, ratings_list)))

"""Duplicates"""


# def return_dups(an_iterable):
#     dups = []
#     a_set = set()

#     for item in an_iterable:
#         l1 = len(a_set)
#         a_set.add(item)
#         l2 = len(a_set)
#         if l1 == l2:
#             dups.append(item)
#     return dups


# a_list = ["Susan Adams", "Kwame Goodall", "Jill Hampton", "Susan Adams"]

# dups = return_dups(a_list)
# print(dups)
