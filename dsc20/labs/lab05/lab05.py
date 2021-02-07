"""
DSC 20 Lab 05
Name: Willis Tan
PID:  A14522499
"""

# Question 1.1
def count_letters(inpath):
    """
    Read in a file and return a dictionary with the counts of all characters
    (including spaces and all other symbols).

    >>> count_letters("infiles/blank.txt")
    {}
    >>> count_letters("infiles/input1.txt")
    {'H': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, '.': 1, '\\n': 1, 'a': 5}
    >>> count_letters("infiles/input3.txt")
    {'a': 3}
    """
    # YOUR CODE GOES HERE #
    out = {}
    with open(inpath, 'r') as f:
        text = f.read()
        for char in text:
            if char in out:
                out[char] += 1
            else:
                out[char] = 1
    return out


# Question 1.2
def count_letters_multiple_files(*inpaths):
    """
    Read in files and return a dictionary with the counts of all characters
    in all the files combined (including spaces and all other symbols).

    >>> count_letters_multiple_files("infiles/input1.txt",
    ... "infiles/blank.txt")
    {'H': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, '.': 1, '\\n': 1, 'a': 5}
    >>> count_letters_multiple_files("infiles/input2.txt")
    {'z': 7, '\\n': 6}
    >>> count_letters_multiple_files('infiles/blank.txt',
    ... 'infiles/input2.txt', 'infiles/input3.txt')
    {'z': 7, '\\n': 6, 'a': 3}
    """
    # YOUR CODE GOES HERE #
    out = {}
    counts = [count_letters(path) for path in inpaths]

    for dictionary in counts:
        for key, value in dictionary.items():
            out.setdefault(key, 0)
            out[key] += value
    return out


# Question 2
def find_intersection(lst1, lst2):
    """
    A function that takes two lists (lst1 and lst2), and finds all items in
    lst2 that also occur in lst1. Return all overlapping items in a list,
    whose items are in the same order as lst2 (i.e. items appear earlier in
    lst2 should also appear earlier in the returned list).

    Note that this function should preserve all intersecting values as many
    times as they occur in both lists.

    >>> find_intersection([1, 2, 3, 4], [1, 2, 1, 2])
    [1, 2]
    >>> find_intersection(['a', 'b', 'c', 'c'], ['c', 'c', 'd', 'e'])
    ['c', 'c']
    >>> find_intersection([1, 2, 3], [])
    []
    """
    # YOUR CODE GOES HERE #
    out = []
    for elem in lst2:
        if elem in lst1:
            try:
                lst1.remove(elem)
            except ValueError:
                break
            out.append(elem)
    return out


# Question 3
def process_dict(data):
    """
    Process the input dictionary with the rules below.
    You can assume that all key-value pairs are non-negative integers.

    For each key in the dictionary:
    - if the key is odd, remove this key-value pair from the dictionary.
    - else if the square of this key exists in the dictionary, square the
        current key's corresponding value. Do not modify the key itself.
    - else if the square root of this key exists in the dictionary,
        square root the current key's corresponding value and convert it
        to int (with int()). Do not modify the key itself.
    - otherwise, don't modify this key and its corresponding value.

    >>> process_dict({1: 1, 2: 2, 3: 3, 4: 4})
    {2: 4, 4: 2}
    >>> process_dict({})
    {}
    >>> process_dict({10: 10, 100: 100, 4: 1})
    {10: 100, 100: 10, 4: 1}
    """
    # YOUR CODE GOES HERE #
    out = {}
    for key, value in data.items():
        if key % 2 != 0:
            continue
        elif key**2 in data:
            out[key] = int(value**2)
        elif key**0.5 in data:
            out[key] = int(value**0.5)
        else:
            out[key] = value
    return out


# Question 4
def determine_siblings(str1, str2):
    """
    A function that checks if two string arguments are siblings.

    We define two strings as siblings if we can rearrange one string to form
    another. For instance, we can rearrange "aabbcde" to form "abedcba" since
    they have the same occurrences of characters, but we cannot rearrange
    "abcdefg" to "xyzabcd".

    >>> determine_siblings("abc", "cba")
    True
    >>> determine_siblings("friend", "aba")
    False
    >>> determine_siblings("ccc", "aba")
    False
    """
    # YOUR CODE GOES HERE #
    return sorted(list(str1)) == sorted(list(str2))


# Question 5
def create_piecewise_function(*cases):
    """
    Given a list of cases as (lower_bound, upper_bound, subfunction) tuples,
    return a piecewise function that takes a numeric argument and apply the
    correct subfunction to the input.

    >>> f_x = create_piecewise_function( \
        (-float('inf'), -1, lambda num: -3 - num), \
        (1, float('inf'), lambda num: num * 3 + 1))
    >>> f_x(-2)
    -1
    >>> f_x(-1)
    -1
    >>> f_x(1)
    4
    """
    # YOUR CODE GOES HERE #
    def func(x):
        for case in cases:
            if case[0] <= x < case[1]:
                return case[2](x)
        return x
    return func
