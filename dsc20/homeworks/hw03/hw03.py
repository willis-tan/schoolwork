"""
DSC 20 Homework 03
Name: Willis Tan
PID:  A14522499
"""


# Question 1
def assert_playground(num, lst, *args, **kwargs):
    """
    ##############################################################
    Requirements:
    1. num must be a positive float
    2. lst must be a list of numbers, the sum of all elements in lst must be
    greater than 10
    3. All values of args must be float, and must be within the range -5.0 to
    -1.0, inclusive
    4. All values in kwargs must be strings, have a length greater than 1, and
    its second character must be "S"
    ##############################################################

    >>> assert_playground(1.5, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    1.5
    >>> assert_playground(15, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(1.5, [0, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    Traceback (most recent call last):
    AssertionError

    NEW DOCTESTS
    >>> assert_playground(0.0, [11.0], -5.0, -1.0, s1=" S", s2="sSs")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(0.1, [10.0, 0.0, 0.01], -5, -1, s1=" S", s2="sSs")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(99.9, (11.0), -5.0, -1.0, s1="_S", s2="sSs")
    Traceback (most recent call last):
    AssertionError
    """
    ARGS_LOWER_BOUND = -5.0
    ARGS_UPPER_BOUND = -1.0
    LST_SUM_LOWER_BOUND = 10

    assert isinstance(num, float) and num > 0.0
    assert isinstance(lst, list)

    assert all(isinstance(x, (int, float)) for x in lst)

    assert sum(lst) > LST_SUM_LOWER_BOUND

    assert all(isinstance(y, float) for y in args)
    assert any([True for z in args if ARGS_LOWER_BOUND <= z <= \
        ARGS_UPPER_BOUND])

    for key in kwargs:
        value = kwargs[key]
        assert isinstance(value, str) and len(value) > 1 and value[1] == "S"

    return num


# Question 2
def various_types(lst):
    """
    ##############################################################
    For each element in the input list:
    If it's a boolean, change to its opposite
    If it's a string, reverse the string
    If it's an integer, square it
    If it's a list, change it to its length
    If it's any other type, change to None

    Return the transformed input list.
    ##############################################################

    >>> various_types(['Hello', 4, ['A', 'B', 'C'], True])
    ['olleH', 16, 3, False]
    >>> various_types([])
    []
    >>> various_types([False, 0, 1, [], 'olleH', ('a', 'b')])
    [True, 0, 1, 0, 'Hello', None]

    NEW DOCTESTS
    >>> various_types(('Hello', 4, ['A', 'B', 'C'], True))
    Traceback (most recent call last):
    AssertionError
    >>> various_types([-1, None, 'abba', (not True), [[1, 2, 3, 4]]])
    [1, None, 'abba', True, 1]
    >>> various_types(['', [[]], (1 < 0)])
    ['', 1, True]
    """
    assert isinstance(lst, list)

    SQUARE = 2

    transformed = [
                    not elem if isinstance(elem, bool) \
                    else elem[::-1] if isinstance(elem, str) \
                    else elem**SQUARE if isinstance(elem, int) \
                    else len(elem) if isinstance(elem, list) \
                    else None \
                    for elem in lst
                ]
    return transformed


# Question 3
def find_greatest_divisor(lower, upper):
    """
    ##############################################################
    Given a lower and upper number, a dictionary where its keys will be all
    integers between lower and upper (inclusive) and their values will be the
    greatest integer in the range 1 to 9 (inclusive) that divides the key.
    ##############################################################

    >>> find_greatest_divisor(20, 27)
    {20: 5, 21: 7, 22: 2, 23: 1, 24: 8, 25: 5, 26: 2, 27: 9}
    >>> find_greatest_divisor(1, 10)
    {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 5}
    >>> find_greatest_divisor(11, 19)
    {11: 1, 12: 6, 13: 1, 14: 7, 15: 5, 16: 8, 17: 1, 18: 9, 19: 1}
    >>> find_greatest_divisor(98, 25)
    Traceback (most recent call last):
    AssertionError

    NEW DOCTESTS
    >>> find_greatest_divisor(0, 0)
    {0: 9}
    >>> find_greatest_divisor(-20, -12)
    {-20: 5, -19: 1, -18: 9, -17: 1, -16: 8, -15: 5, -14: 7, -13: 1, -12: 6}
    >>> find_greatest_divisor(-1, 0.0)
    Traceback (most recent call last):
    AssertionError
    """
    assert isinstance(lower, int) and isinstance(upper, int)
    assert lower <= upper

    MAX_DIVISOR = 9
    
    divisors = [x for x in range(MAX_DIVISOR, 0, -1)]
    numbers = [y for y in range(lower, upper + 1)]
    
    output = {}
    for i in numbers:
        for j in divisors:
            if i % j == 0:
                output[i] = j
                break
    return output


# Question 4
def best_player(**player_scores):
    """
    ##############################################################
    Each player and their list of scores will be passed as keyword arguments in
    the form: keyword: <name>, value: <list of positive numeric scores>

    The truncated mean score of each player's scores will be calculated, and
    the name of the player with the highest score will returned.

    Assumptions:
    1. At least 1 score list is passed in the function. Each score list has at
       least 3 elements.
    2. If there are multiple highest or lowest scores in a score list,
       remove one of each and keep the rest.
    3. If there are multiple best players, return any of them.

    ##############################################################

    >>> best_player(marina=[9.6, 9, 9.8, 9.9], yuxuan=[9.0, 9.5, 9.9],
    ... elvy=[10.0, 9.8, 10.0, 9.5, 9.6])
    'elvy'
    >>> best_player(sean=[100, 99.99, 100])
    'sean'
    >>> best_player(james=[3.8, 3.5, 3.2], simon=[4.0, 3.6, 3.0])
    'simon'

    NEW DOCTESTS
    >>> best_player(james=[7, 7.0, 7], earl=[7, 7, 10.0], jones=[1, 7, 7])
    'james'
    >>> best_player(james=[7, 7.0, 7], earl=(7, 7, 10.0), jones=[1, 7, 7])
    Traceback (most recent call last):
    AssertionError
    >>> best_player(james=7, earl=[7, 7, 10.0], jones=[1, 7, 7])
    Traceback (most recent call last):
    AssertionError
    """
    for name in player_scores:
        assert isinstance(name, str)
        scores = player_scores[name]
        assert isinstance(scores, list)
        assert all(isinstance(x, (int, float)) and x > 0 for x in scores)

    sort_scores = lambda x: sorted(x)[1:-1]
    avg_score = lambda y: sum(y) / len(y)
    trunc_scores = [
        (name, avg_score(sort_scores(player_scores[name]))) \
        for name in player_scores
    ]
    return max(trunc_scores, key = lambda i : i[1])[0] 


# Question 5
def deserialize(outpath, patterns, *serialized_lines):
    """
    ##############################################################
    Takes a list of string patterns and lists of counts, where each list of
    counts represent one line, the function decodes the list of patterns for
    each line and writes each line to the outpath file. For each number in a
    list of counts, write the corresponding element in the patterns list X
    times on the file. If there are n elements in the patterns list and a list
    of counts has >n elements, than the n+1 element in the list of counts
    corresponds to the 1st element of the patterns list. The n+2 element
    corresponds the the 2nd element of the patterns list, and so on. Repeat as
    many times as necessary.

    Example:
    Patterns list = ["a", "b", "c"]
    Serialized lines (list of counts) = [1, 2, 3], [5, 1, 0, 4]

    The first list [1, 1, 1] means write 1 "a", 2 "b", and 3 "c" as the first 
    line.
    The second list [5, 1, 0, 4] means write 5 "a", 1 "b", 0 "c", and 4 "a" on
    the second line.

    The outpath file should have this as the first 2 lines:
    abbccc
    aaaaabaaaa
    ##############################################################

    >>> deserialize("outfiles/out1.txt", ["**", "Marina"],
    ... [1,1,1], [0,5], [3,3,0,3,3])
    >>> with open("outfiles/out1.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    **Marina**
    MarinaMarinaMarinaMarinaMarina
    ******MarinaMarinaMarinaMarinaMarinaMarina******

    >>> deserialize("outfiles/out2.txt", ["__", "()", "??"],
    ... [2,4,0,2], [1,2,0,2,2,0,1], [0,2,0,4,2,0], [0,1,0,6,1,0])
    >>> with open("outfiles/out2.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    ____()()()()____
    __()()____()()__
    ()()________()()
    ()____________()

    >>> deserialize("outfiles/out3.txt", ["##", "__"],
    ... [2,3,2,2,2,1,2,3,1,1], [1,1,1,1,1,3,1,5,1,1,1,1,1],
    ... [1,1,1,2,1,2,1,4,1,2,1,1,1], [1,1,1,3,1,1,1,3,1,3,1,1,1],
    ... [2,2,2,3,2,1,3,2,1,1])
    >>> with open("outfiles/out3.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    ####______####____####__####______##__
    ##__##__##______##__________##__##__##
    ##__##____##____##________##____##__##
    ##__##______##__##______##______##__##
    ####____####______####__######____##__

    NEW DOCTESTS
    >>> deserialize("outfiles/test1.txt", ["__", "||"],
    ... [0,1,1,1], [1,1,1])
    >>> with open("outfiles/test1.txt", "r") as testfile1:
    ...     print(testfile1.read().strip())
    ||__||
    __||__

    >>> deserialize("outfiles/test2.txt", ["X", "YY", "Z"],
    ... [0,1,2,3], [0,2,4,6], [1,0,0,1])
    >>> with open("outfiles/test2.txt", "r") as testfile2:
    ...     print(testfile2.read().strip())
    YYZZXXX
    YYYYZZZZXXXXXX
    XX

    >>> deserialize("outfiles/test3.txt", ["^", "(- _ -)", "Z", "z"],
    ... [0,1,0,0,4,0,1,2])
    >>> with open("outfiles/test3.txt", "r") as testfile3:
    ...     print(testfile3.read().strip())
    (- _ -)^^^^Zzz
    """
    tups_to_string = lambda x: x[0] * x[1]
    with open(outpath, "w") as f:
        
        for line in serialized_lines:
            tups = []
            n = len(patterns)
            i = 0
            while True:
                j = 0
                while j < len(line):
                    if i == n: 
                        i = 0
                    tups.append((patterns[i], line[j]))
                    i += 1
                    j+=1
                break
            f.write("".join(list(map(tups_to_string, tups))) + '\n')

    f.close()
    return None


# Question 6
def sequential_apply(nums, *instructions):
    """
    ##############################################################
    Transforms a list of numbers sequentially based on the commands that are
    passed in instructions. The instructions will be a list of tuples as
    follows:

    ('add', k) -> Add k to each element of the current list
    ('multiply', k) -> Multiply each element of the current list by k
    ('insert', i, k) -> Insert the value k at index i of the current list
    ('remove', i) -> Remove the element at index i of the current list
    ('mean',) -> Replace each element with the mean of the current list
    ('range',) -> Replace each element with the range of the current list

    Return the list after transformations are complete
    ##############################################################

    Examples of all instructions:
    [1, 2, 3, 4], ('add', 1) -> [2, 3, 4, 5]
    [1, 2, 3, 4], ('multiply', 2) -> [2, 4, 6, 8]
    [1, 2, 3, 4], ('insert', 1, 100) -> [1, 100, 2, 3, 4]
    [1, 2, 3, 4], ('remove', 1) -> [1, 3, 4]
    [1, 2, 3, 4], ('mean',) -> [2.5, 2.5, 2.5, 2.5]
    [1, 2, 3, 4], ('range',) -> [3, 3, 3, 3]

    >>> sequential_apply([1, 2, 3, 4], ('add', 1))
    [2, 3, 4, 5]
    >>> sequential_apply([3.3, 6.6, 7.7],
    ... ('insert', 1, 5.5), ('insert', 1, 4.4))
    [3.3, 4.4, 5.5, 6.6, 7.7]
    >>> sequential_apply([9.9, 1.3, 8.2, 4, 10],
    ... ('remove', 0), ('mean',), ('range',), ('add', 10))
    [10.0, 10.0, 10.0, 10.0]

    NEW DOCTESTS
    >>> sequential_apply([1, 2, 3, 4], ('remove', 1), ('remove', 1), 
    ... ('remove', 1), ('range', ))
    [0]
    >>> sequential_apply([-7])
    [-7]
    >>> sequential_apply([1, 2, 3, 4], ('add', -1), ('mean', ), 
    ... ('insert', 1, 0), ('multiply', -1.0))
    [-1.5, -0.0, -1.5, -1.5, -1.5]
    """
    assert isinstance(nums, list) and \
        all(isinstance(x, (int, float)) for x in nums)

    INSERT_INDEX = 2
    for query in instructions:
        func = query[0]
        if func == 'insert':
            nums.insert(query[1], query[INSERT_INDEX])
        elif func == 'remove':
            del nums[query[1]]
        elif func == 'add':
            nums = [x + query[1] for x in nums]
        elif func == 'multiply':
            nums = [x * query[1] for x in nums]
        elif func == 'mean':
            nums = [sum(nums) / len(nums) for x in nums]
        elif func == 'range':
            nums = [max(nums) - min(nums) for x in nums]
    return nums
