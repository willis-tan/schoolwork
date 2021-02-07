"""
DSC 20 Homework 06
Name: Willis Tan
PID:  A14522499
"""


# Question 1
def hate_f(word):
    """
    Recursively remove all "f" and "F" characters from the input string and
    return the string without those characters.

    >>> hate_f('FabFxx')
    'abxx'
    >>> hate_f('FfFf')
    ''
    >>> hate_f('ABCde')
    'ABCde'

    NEW DOCTESTS
    >>> hate_f('')
    ''
    >>> hate_f('f')
    ''
    >>> hate_f('F')
    ''
    """
    # YOUR CODE GOES HERE #
    if len(word) == 0:
        return ''
    elif word[0] != 'F' and word[0] != 'f':
        return word[0] + hate_f(word[1:])
    else:
        return '' + hate_f(word[1:])


# Question 2
def encode(mapping, plaintext):
    """
    Given a mapping dictionary and an input string, the function will
    recursively map each character in the input string to its value in the
    mapping dictionary. After all the mappings are complete, the resulting
    string is returned.

    Keys in the mapping dictionary are strings of length 1
    Values in the mapping dictionary are strings of length 3

    >>> mapping = {'z': 'not', 'r': 'ece', 't': 'dsc'}
    >>> encode(mapping, 'zzr')
    'notnotece'
    >>> encode(mapping, 'zzt')
    'notnotdsc'
    >>> encode(mapping, 'ttzrr')
    'dscdscnoteceece'

    NEW DOCTESTS
    >>> map1 = {'z': 'xxx', 'o': 'xxx', 't': 'yyy', 'p': 'yyy'}
    >>> encode(map1, 'zztop')
    'xxxxxxyyyxxxyyy'

    >>> map2 = {'z': '000', 'o': '000', 't': '000', 'p': '000'}
    >>> encode(map2, 'zztop')
    '000000000000000'

    >>> map3 = {'x': '11x', ' ': '_._', '+': '_+_', 'y': '11y'}
    >>> encode(map3, 'x + y')
    '11x_.__+__._11y'
    """
    # YOUR CODE GOES HERE #
    if len(plaintext) == 0:
        return ''
    elif plaintext[0] in mapping:
        return mapping[plaintext[0]] + encode(mapping, plaintext[1:])
    else:
        return '' + encode(mapping, plaintext[1:])


# Question 3
def climb_stair(n_steps):
    """
    Given a number of steps a stair has, recursively find the number of
    different ways to walk up this stair.

    Either one or two steps can be walked up at a time.

    >>> climb_stair(2)
    2
    >>> climb_stair(5)
    8
    >>> climb_stair(8)
    34

    NEW DOCTESTS
    >>> climb_stair(1)
    1
    >>> climb_stair(20)
    10946
    >>> climb_stair(3)
    3
    """
    # YOUR CODE GOES HERE #
    WALK_TWO_STEP = 2

    if n_steps == 1:
        return 1
    elif n_steps == WALK_TWO_STEP:
        return WALK_TWO_STEP

    return climb_stair(n_steps - 1) + climb_stair(n_steps - WALK_TWO_STEP)
    


# Question 4
def add_all_digits(num):
    """
    Given any nonnegative integer, recursively add up every digit in the
    number. If the sum of the digits is less than 10, return the sum. Else,
    recursively add the digits again until a sum of less than 10 is produced.

    >>> add_all_digits(41)
    5
    >>> add_all_digits(567)
    9
    >>> add_all_digits(999777)
    3

    NEW DOCTESTS
    >>> add_all_digits(0)
    0
    >>> add_all_digits(1000000000)
    1
    >>> add_all_digits(1000000000000000009)
    1
    """
    # YOUR CODE GOES HERE #
    UPPER_BOUND = 10

    if 0 <= num < UPPER_BOUND:
        return num
    else:
        to_str = str(num)
        summation = 0
        for i in to_str:
            summation += int(i)
        return add_all_digits(summation)


# Question 5
def find_max_recursive(lst):
    """
    Given an input list, recursively find the maximum element that is in the
    list.

    >>> find_max_recursive([1, 2, 3, 4, 5])
    5
    >>> find_max_recursive([10, 11, 5, 0, -10, 1])
    11
    >>> find_max_recursive(['b', 'c', 'z', 'y', 'a', 'e'])
    'z'

    NEW DOCTESTS
    >>> find_max_recursive([1, 1, 1, 1, 1, 1])
    1
    >>> find_max_recursive([''])
    ''
    >>> find_max_recursive([100, 7, -30, 99, -66, 100])
    100
    """
    # YOUR CODE GOES HERE #
    if len(lst) == 1:
        return lst[0]
    
    m = find_max_recursive(lst[1:])
    if m > lst[0]:
        return m
    else:
        return lst[0]


# Question 6
def skip_then_swap(string, n_skip, n_swap):
    """
    Given an input string, the first n_skip characters and last n_skip
    characters are skipped (no alterations). 

    Then, the (n_skip+1)th character is swapped with the (n_skip+1)th to last
    character. Repeat with the next character. In total, this is done n_swap
    times.

    The rest of the characters in the middle are left untouched.

    Return the resulting transformed string.

    >>> skip_then_swap('kkkABXXXXCDkkk', 3, 2)
    'kkkDCXXXXBAkkk'
    >>> skip_then_swap('DSC20', 1, 2)
    'D2CS0'
    >>> skip_then_swap('skip_then_swap', 4, 3)
    'skip_neht_swap'

    NEW DOCTESTS
    >>> skip_then_swap('beta zeta', 1, 1)
    'btta zeea'
    >>> skip_then_swap('abcde', 0, 3)
    'edcba'
    >>> skip_then_swap('unchanged', 3, 0)
    'unchanged'
    """
    # YOUR CODE GOES HERE #
    if len(string) == 1:
        return string
    else:
        if n_skip > 0:
            return string[0] \
                + skip_then_swap(string[1:-1], n_skip - 1, n_swap) \
                + string[-1]
        if n_swap > 0:
            return string[-1] \
                + skip_then_swap(string[1:-1], 0, n_swap - 1) \
                + string[0]
        else:
            return string


# Question 7
def flatten_dict(nested_dict):
    """
    Given a dictionary with string keys and possibly another a dictionary as
    values, this function recursively flattens the input dictionary until none
    of its values are dictionaries. If there are no dictionary values, return
    the input as is.

    If there is a key that has a dictionary value, then each key in the
    nested dictionary will be concatenated with the outer key and its value
    will be the inner key's value. This process will keep repeating if there 
    are multiple nested dictionaries.


    >>> flatten_dict({'A': 1, 'B': 2})
    {'A': 1, 'B': 2}
    >>> flatten_dict({'Hi': True, 'Hello': {'World': 'Java',
    ... 'Kitty': 'Python'}})
    {'Hi': True, 'HelloWorld': 'Java', 'HelloKitty': 'Python'}
    >>> flatten_dict({'A': {'B': 1, 'C': 2, 'D': {'E': 3, 'F': 4}},
    ... 'G': 5, 'H': 6})
    {'AB': 1, 'AC': 2, 'ADE': 3, 'ADF': 4, 'G': 5, 'H': 6}

    NEW DOCTESTS
    >>> flatten_dict({'Hello': {'World': 'Java', 'Kitty': {'Python': 'Dog'}}})
    {'HelloWorld': 'Java', 'HelloKittyPython': 'Dog'}
    >>> flatten_dict({'A': \
                        {'A': \
                            {'A': 'A'}}})
    {'AAA': 'A'}
    >>> flatten_dict({'a': {'a': 'a', 'b': 'b'}, 'b': {'a': 'a', 'b': 'b'}})
    {'aa': 'a', 'ab': 'b', 'ba': 'a', 'bb': 'b'}
    """
    # YOUR CODE GOES HERE #
    out = dict()
    for k, v in nested_dict.items():
        if not isinstance(v, dict):
            out[k] = v
        else:
            inner = flatten_dict(v)
            for key in inner:
                out[k + key] = inner[key]
    return out
