"""
DSC 20 Homework 04
Name: Willis Tan
PID:  A14522499
"""


# Utility Function
def is_iterable(obj):
    """
    A function that checks if `obj` is a iterable (can be iterated over
    in a for-loop).

    DO NOT MODIFY THIS FUNCTION. You don't need to add new doctests
    for this function.

    >>> is_iterable(1)
    False
    >>> is_iterable("DSC 20")
    True
    >>> is_iterable(["Fall", 2020])
    True
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False


# Question 1
def ucsd_spam_quarantine(emails, allowlist, blocklist):
    """
    ##############################################################
    This function filters out malicious emails from the input emails list.
    A list of all safe emails is returned.

    A malicious email is an email that is in the blocklist, does not end with
    "ucsd.edu", or is not in the blocklist.
    ##############################################################

    >>> emails = ["mlanglois@ucsd.edu", "istudents@ucsd.edu", \
    "jsmith@eng.ucsd.edu", "hello@gmail.com", "python@yahoo.com", \
    "phish@ucsd.edu"]
    >>> allowlist = ["hello@gmail.com"]
    >>> blocklist = ["phish@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['mlanglois@ucsd.edu', 'istudents@ucsd.edu', \
'jsmith@eng.ucsd.edu', 'hello@gmail.com']

    >>> emails = ["sean@ucsd.edu", "jojo@ucsd.edu", "dsc@ucsd.edu.us", \
    "tritons@outlook.com", "spam@ucsd.edu", "bad@ucsd.edu"]
    >>> allowlist = ["tritons@outlook.com", "no-reply@piazza.com"]
    >>> blocklist = ["spam@ucsd.edu", "bad@ucsd.edu", "phish@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['sean@ucsd.edu', 'jojo@ucsd.edu', 'tritons@outlook.com']
    """
    # YOUR CODE GOES HERE #
    assert(all(isinstance(x, list) for x in [emails, allowlist, blocklist]))

    func = lambda x: True if (x in allowlist or x[-8:] == "ucsd.edu") \
                     and x not in blocklist \
                     else False
    
    return list(filter(func, emails))


# Question 2
def create_dsc_email(students, years):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> students = [ \
        ("First Middle Last", 2022, "revelle", "DS25"), \
        ("hi HELLO", 2022, "seventh", "DS25"), \
        ("Computer Science", 2021, "Warren", "CS25"), \
        ("longfirstname longlastname", 1990, "Marshall", "DS25") \
    ]
    >>> create_dsc_email(students, [2022])
    {'First Middle Last': 'firlast22rc@dsc.ucsd.edu', \
'hi HELLO': 'hihello22sv@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [1990, 2021])
    {'longfirstname longlastname': 'lonlongla90tm@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [])
    {}
    """
    # YOUR CODE GOES HERE #
    return ...


# Question 3
def base_converter(target_base):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> binary_converter = base_converter(2)
    >>> [binary_converter(i) for i in range(10)]
    ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']
    >>> base_converter(16)(8200)
    '2008'
    >>> base_converter(36)(8200)
    '6BS'
    """
    # YOUR CODE GOES HERE #
    return ...


# Question 4
def magic_sequence_generator(start0, start1, start2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> gen = magic_sequence_generator(10, 20, 30)
    >>> [next(gen) for _ in range(3)]
    [10, 20, 30]
    >>> next(gen)
    0
    >>> [next(gen) for _ in range(10)]
    [50, 20, 30, 40, 10, 60, 10, 60, 10, 60]
    """
    # YOUR CODE GOES HERE #
    return ...


# Question 5
def round_robin_generator(k, arg1, arg2, arg3):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> arg1 = "abcdefgh"
    >>> arg2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> arg3 = (True, False, True, False, True, False)
    >>> gen = round_robin_generator(2, arg1, arg2, arg3)
    >>> [next(gen, None) for _ in range(14)]
    ['a', 'b', 1, 2, True, False, 'c', 'd', 3, 4, True, False, 'e', 'f']

    >>> gen = round_robin_generator(3, arg1, arg2, arg3)
    >>> [next(gen, None) for _ in range(14)]
    ['a', 'b', 'c', 1, 2, 3, True, False, True, 'd', 'e', 'f', 4, 5]

    >>> arg4 = "dsc"
    >>> arg5 = [2, 0]
    >>> arg6 = "fall"
    >>> gen = round_robin_generator(4, arg4, arg5, arg6)
    >>> [next(gen, None) for _ in range(10)]
    ['d', 's', 'c', None, 2, 0, None, None, 'f', 'a']
    """
    # YOUR CODE GOES HERE #
    return ...


# Question 6
def make_generator(*args):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> gen1 = make_generator(10, 20, 30)
    >>> [next(gen1, None) for _ in range(10)]
    [10, 20, 30, 0, 50, 20, 30, 40, 10, 60]
    >>> gen2 = make_generator([10, 20], "Sean", [True, False])
    >>> [next(gen2, None) for _ in range(10)]
    [10, 20, 'S', 'e', True, False, None, None, 'a', 'n']
    >>> gen3 = make_generator("Ev", 0, ["en"], ("DD",))
    >>> [next(gen3, None) for _ in range(10)]
    ['Ev', ['en'], 0, ('DD',), None, None, None, None, None, None]
    """
    # YOUR CODE GOES HERE #
    return ...


# Question 7
def skip_increasing(iterable, k):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> skip_increasing(iter([1,2,3,4,5,6,7,8,9,10,11]), 5)
    [1, 2, 4, 7, 11]
    >>> skip_increasing(iter('ABcDefGhijKlmnoPqrs'), 10)
    ['A', 'B', 'D', 'G', 'K', 'P']
    >>> skip_increasing(iter((1, None, 3, 4, 5, 6, 7, 8)), 3)
    [1, None, 4]
    """
    # YOUR CODE GOES HERE #
    return ...
