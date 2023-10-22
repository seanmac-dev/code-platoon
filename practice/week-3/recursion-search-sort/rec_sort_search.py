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


sorted_fruits = ["apple", "banana", "orange", "plum"]
print(bisect_left(sorted_fruits, "banana"))
# prints index of banana: 1
# will also return where an item would go if it were in your iterable
# "kiwi" would go in index 2, but to check we have to do the below:


def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False


print(binary_search(["a", "c", "e", "p"], "e"))
