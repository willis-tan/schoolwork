"""
DSC 20 Lab 04
Name: Willis Tan
PID:  A14522499
"""


# Question 1
def dict_to_string(data, is_key):
    """
    A function that concatenates all keys (when is_key is True)
    or all values (when is_key is False) of the `data` dictionary
    to a string, where each item is at its own line.

    >>> data = {'USA': 'Washington, D.C.', \
        'Russia': 'Moscow', 'France': 'Paris'}
    >>> dict_to_string(data, True)
    'USA\\nRussia\\nFrance'
    >>> print(dict_to_string(data, True))
    USA
    Russia
    France
    >>> print(dict_to_string(data, False))
    Washington, D.C.
    Moscow
    Paris
    """
    
    if is_key == True:
        return "\n".join([key for key in data])
    else:
        return "\n".join(data.values())


# Question 2
def palindrome_checker():
    """
    Returns a lambda function which takes a string as input, and checks
    whether the input is a palindrome string (ignore spaces). You may assume
    that the returned lambda function only takes a string with lowercase
    letters and spaces only.

    You should NOT use loops and list comprehension for this question.

    >>> palindrome_checker()("top spot")
    True
    >>> palindrome_checker()("abcdefg")
    False
    >>> palindrome_checker()("racecar")
    True
    """
    
    return lambda x: x.replace(" ", "") == x.replace(" ", "")[::-1]


# Question 3
def find_good_numbers(nums):
    """
    A function that finds all good numbers (integers divisible by 11 or 7)
    in a list of integers and return them in a list.

    You should NOT use loops and list comprehension for this question.

    >>> find_good_numbers([19, 65, 57, 39, 152, 639, 121, 44, 90, 190, 132])
    [121, 44, 132]
    >>> find_good_numbers([7, 11])
    [7, 11]
    >>> find_good_numbers([])
    []
    """
    
    func = lambda x: (x % 7 == 0) or (x % 11 == 0)
    return list(filter(func, nums))


# Question 4
def increment_list(nums, amount):
    """
    A function that takes a list of numbers and an amount to increment,
    increment all numbers in the list by the specified amount if the amount
    is nonnegative, and return the incremented list.

    You should NOT use loops and list comprehension for this question.

    >>> increment_list([1, 2, 3], 10)
    [11, 12, 13]
    >>> increment_list([1, 2, 3], -1)
    [1, 2, 3]
    >>> increment_list([2, 9, 10], 0)
    [2, 9, 10]
    """
    
    func = lambda x: (x + amount) if amount >= 0 else x
    return list(map(func, nums))


# Question 5
def filter_then_map(lst, func_filter, func_map):
    """
    A function that takes a list (`lst`), a function to use with the filter
    method (`func_filter`) and a function to use with the map method
    (`func_map`), and return the list after applying filter and map
    with the specified functions sequentially. You may assume that the
    provided functions will not cause any errors when applying to the elements
    in `lst`.

    You should NOT use loops and list comprehension for this question.

    >>> filter_then_map(['Marina', 'Yuxuan', 'Jerry', 'Elvy'], \
        lambda name: len(name) < 6, lambda name: name.upper())
    ['JERRY', 'ELVY']
    >>> filter_then_map([1, 1.0, 2, 2.0, 3, 3.0, 4, 4.0, 5, 5.0], \
        lambda num: isinstance(num, int), float)
    [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> filter_then_map([0, lambda x: x + 1, lambda x: x * 2], \
        callable, lambda func: func(100))
    [101, 200]
    """
    # YOUR CODE GOES HERE #
    return list(map(func_map, filter(func_filter, lst)))


# Question 6
def binarize_matrix(matrix, threshold):
    """
    A function that takes a matrix (2D list with numeric values) and a
    threshold, and returns the binarized matrix. To binarize a matrix,
    each element smaller than the threshold is changed to 0, and other
    elements are changed to 1.

    You should NOT use loops and list comprehension for this question.

    >>> binarize_matrix([[1, -2, -3], [-4, 5, -6], [-7, -8, 9]], 0)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> binarize_matrix([[-0.6, -1.2], [-7, -3.5]], -5.5)
    [[1, 1], [0, 1]]
    >>> binarize_matrix([[12.5, 4.8, -3], [-9, 1.2, 4.2], [0.1, 2.2, 1]], 20)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    # YOUR CODE GOES HERE #
    func1 = lambda x: 0 if x < threshold else 1
    func2 = lambda y: list(map(func1, y))
    return list(map(func2, matrix))


# Question 7
def triple_map(func, iterable):
    """
    A generator that iterates through each item in the `iterable`,
    apply the given function `func` for three times and yield the result.
    You may assume `func` takes only 1 argument and can be applied to
    all elements in the `iterable` without any error. You should not use
    the built-in map() function.

    >>> gen = triple_map(lambda num: num + 3, range(1, 100, 3))
    >>> print(next(gen))
    10
    >>> print(next(gen))
    13
    >>> [next(gen) for _ in range(5)]
    [16, 19, 22, 25, 28]
    """
    # YOUR CODE GOES HERE #
    for i in iterable:
        yield func(func(func(i)))


# Question 8
def repeat_apply_functions(elem, n_repeat, *funcs):
    """
    Given an element of any type (`elem`), functions that can be applied
    to this element without any error (`*funcs`) and the number of times
    these functions will be applied (`n_repeat`), apply all functions to
    the element sequentially in the given order for `n_repeat` times.

    >>> repeat_apply_functions('Marina', 2, \
        lambda text: text + '!', lambda text: text * 2)
    'Marina!Marina!!Marina!Marina!!'
    >>> repeat_apply_functions(10, 3, \
        lambda num: num + 1, lambda num: num + 2, lambda num: num + 3)
    28
    >>> repeat_apply_functions([], 4, \
        lambda lst: lst + [0], lambda lst: lst + [1])
    [0, 1, 0, 1, 0, 1, 0, 1]
    """
    # YOUR CODE GOES HERE #
    for i in range(n_repeat):
        for j in funcs:
            elem = j(elem)
    return elem
