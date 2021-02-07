"""
DSC 20 Homework 08
Name: Willis Tan
PID:  A14522499
"""

# Question 1
def counter_doctests():
    """
    Doctests for Counter and AlphanumericCounter.

    >>> counter = Counter()
    >>> counter.size()
    0
    >>> counter.add_items([123, 123, "abc", (10, 10), (10, 20)])
    >>> counter.size()
    5
    >>> counter.get_count(123)
    2
    >>> counter.get_count("dsc20")
    0
    >>> counter.get_all_counts()
    {123: 2, 'abc': 1, (10, 10): 1, (10, 20): 1}

    >>> an_counter = AlphanumericCounter()
    >>> an_counter.size()
    0
    >>> len(an_counter.counts)
    62
    >>> an_counter.add_items("DSC 20 (Marina Langlois)")
    >>> an_counter.size()
    19
    >>> an_counter.get_count("a")
    3
    >>> an_counter.get_count("?")
    0
    >>> an_counter.get_all_counts()
    {'0': 1, '2': 1, 'a': 3, 'g': 1, 'i': 2, 'l': 1, 'n': 2, 'o': 1, \
'r': 1, 's': 1, 'C': 1, 'D': 1, 'L': 1, 'M': 1, 'S': 1}


    Counter Instance:
    >>> test_counter = Counter()

    >>> test_counter.size()
    0
    >>> test_counter.get_count(('null', 'nan'))
    0
    >>> test_counter.add_items(['e', 'e', 'e', 'e'])
    >>> test_counter.size()
    4
    >>> test_counter.get_count('e')
    4
    >>> test_counter.get_all_counts()
    {'e': 4}
    >>> test_counter.add_items('string')
    >>> test_counter.get_all_counts()
    {'e': 4, 's': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
    >>> test_counter.size()
    10
    >>> test_counter.get_count('t')
    1
    >>> test_counter.add_items(('string', (0, 1), 6))
    >>> test_counter.get_all_counts()
    {'e': 4, 's': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, 'string': 1, \
(0, 1): 1, 6: 1}


    AlphanumericCounter Instance:
    >>> test_anc = AlphanumericCounter()
    
    >>> test_anc.size()
    0
    >>> test_anc.get_count('b')
    0
    >>> test_anc.add_items('eeee')
    >>> test_anc.size()
    4
    >>> test_anc.get_count('e')
    4
    >>> test_anc.get_all_counts()
    {'e': 4}
    >>> test_anc.add_items('Generic string: 1234')
    >>> test_anc.get_all_counts()
    {'1': 1, '2': 1, '3': 1, '4': 1, 'c': 1, 'e': 6, 'g': 1, 'i': 2, 'n': 2, \
'r': 2, 's': 1, 't': 1, 'G': 1}
    >>> test_anc.size()
    21
    >>> test_anc.get_count('t')
    1
    >>> test_anc.add_items('Decimal: 0.56')
    >>> test_anc.get_all_counts()
    {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, 'a': 1, 'c': 2, \
'e': 7, 'g': 1, 'i': 3, 'l': 1, 'm': 1, 'n': 2, 'r': 2, 's': 1, 't': 1, \
'D': 1, 'G': 1}
    """
    return


class Counter:
    """
    The Counter class creates a general counter for any iterable object.
    Each unique item in the iterable has its number of occurences stored in a
    dictionary.
    """

    def __init__(self):
        """
        Constructor for the Counter class. Each Counter instance will have
        attribute nelems and counts.

        nelems: Initialized with 0. Represents the number of items stored.
        counts: Initialized with empty dictionary. Stores all items as keys
        with the count of the item as values 
        """
        # YOUR CODE GOES HERE #
        self.nelems = 0
        self.counts = dict()

    def size(self):
        """
        Getter method for the number of items stored
        """
        # YOUR CODE GOES HERE #
        return self.nelems

    def get_count(self, item):
        """
        Getter method for the count of an item.
        If item is not in counts, return 0.
        """
        # YOUR CODE GOES HERE #
        if item in self.counts:
            return self.counts[item]
        else:
            return 0

    def get_all_counts(self):
        """
        Getter method for the counts dictionary
        """
        # YOUR CODE GOES HERE #
        return self.counts

    def add_items(self, items):
        """
        Given an iterable, store each item in the iterable to the counts
        dictionary.
        """
        # YOUR CODE GOES HERE #
        for i in items:
            if i not in self.counts:
                self.counts[i] = 1
            else:
                self.counts[i] += 1
            self.nelems += 1


class AlphanumericCounter(Counter):
    """
    The AlphanumericCounter class inherits the Counter parent class. This class
    also implements a counter, but only for strings. Given any string,
    Alphanumeric instances will store the alphanumeric characters of the input
    string and their respective counts in a counts list.

    The indices of the counts list represent a certain character as follows:
        If the character is numeric (0-9), its index will be 0 to 9.
        If the character is lowercase letter, its index will be 10 to 35.
        If the character is uppercase letter, its index will be 36 to 61.
    """

    def __init__(self):
        """
        Constructor for the AlphanumericCounter class. Inherits the Counter
        parent class. Has two instance attributes: nelems and counts.

        nelems: Total number of items stored. Initialized with 0
        counts: Initialized as a list of 62 zeroes. Stores the counts of all
        items.
        """
        # YOUR CODE GOES HERE #
        MAX_CHAR = 62

        super().__init__()
        self.counts = [0 for i in range(MAX_CHAR)]

    def get_index(self, item):
        """
        Given an item, return its corresponding index in the counts list.

        If the item is numeric (0-9), its index will be 0 to 9.
        If the item is lowercase letter, its index will be 10 to 35.
        If the item is uppercase letter, its index will be 36 to 61.
        Else, its index will be -1.
        """
        # YOUR CODE GOES HERE #
        ascii_value = ord(item)
        if item.isnumeric():
            return int(item)
        elif item.isupper():
            UPPER_OFFSET = 29
            return ascii_value - UPPER_OFFSET
        elif item.islower():
            LOWER_OFFSET = 87
            return ascii_value - LOWER_OFFSET
        else:
            return -1

    def get_char(self, idx):
        """
        Given an index (0 to 61), return the corresponding item.
        """
        # YOUR CODE GOES HERE #
        MAX_NUM = 9
        MAX_LOWERCASE = 35
        LOWER_OFFSET = 87
        MAX_UPPERCASE = 61
        UPPER_OFFSET = 29

        if 0 <= idx <= MAX_NUM:
            return str(idx)
        elif MAX_NUM < idx <= MAX_LOWERCASE:
            return chr(idx + LOWER_OFFSET)
        elif MAX_LOWERCASE < idx <= MAX_UPPERCASE:
            return chr(idx + UPPER_OFFSET)
        

    def get_count(self, item):
        """
        Given an item, return its count from the counts list.
        If the item is not in the counts list, return 0
        """
        # YOUR CODE GOES HERE #
        if self.get_index(item) != -1:
            return self.counts[self.get_index(item)]
        return 0

    def get_all_counts(self):
        """
        Converts the counts list into a dictionary with item, count as key
        value pairs. If an item has 0 counts, it is not included in the
        dictionary. The resulting dictionary is returned.
        """
        # YOUR CODE GOES HERE #
        return {
            self.get_char(i): self.counts[i] for i in range(len(self.counts)) \
            if self.counts[i] > 0 \
        }

    def add_items(self, items):
        """
        Given a string, every alphanumeric character in the string has its
        count added to the counts list in the corresponding index.
        """
        # YOUR CODE GOES HERE #
        for char in items:
            idx = self.get_index(char)
            if idx != -1:
                self.counts[idx] += 1
                self.nelems += 1


# Question 2
def find_two_sums_rec(main, sub):
    """
    Given two lists of numbers, the function recursively finds the sum of the
    two lists' intersection and the sum of their difference. Hence,

    1. Intersection: Sum of all numbers in main that are also in sub
    2. Difference: Sum of all numbers in main that are not in sub

    The two sums are returned as a tuple, (sum intersection, sum difference)

    If the main list is empty, return the tuple (0, 0)

    >>> main_seq = [0, 1, 1, 2, 3, 3, 4, 5, 5]
    >>> find_two_sums_rec(main_seq, [])
    (0, 24)
    >>> find_two_sums_rec(main_seq, [1, 2])
    (4, 20)
    >>> find_two_sums_rec(main_seq, [3, 4, 5])
    (20, 4)

    NEW DOCTESTS
    >>> find_two_sums_rec([], [])
    (0, 0)
    >>> find_two_sums_rec([1, 0, 0, 1, 1], [0, 1, 2, 3, 4])
    (3, 0)
    >>> find_two_sums_rec([-1, 1, -6.5, 3, 3.5], [-1, 1])
    (0, 0.0)
    """
    # YOUR CODE GOES HERE #
    if len(main) == 0:
        return (0, 0)
    
    last = main[-1]
    copy = main.copy()
    copy.pop()
    if last in sub:
        intersection = last + find_two_sums_rec(copy, sub)[0]
        difference = find_two_sums_rec(copy, sub)[1]
    else:
        intersection = find_two_sums_rec(copy, sub)[0]
        difference = last + find_two_sums_rec(copy, sub)[1]
        
    return (intersection, difference)



# Question 3
def compute_max_string(base, pattern):
    """
    Given a base string and a pattern string, recursively the length of the
    substring that starts with the pattern and ends with pattern.

    Only case sensitive matches are considered.
    The substring can have its start and end pattern fully, partially, or not
    overlap.

    If no such substring exists, return 0.

    >>> compute_max_string("jumpsjump", "jump")
    9
    >>> compute_max_string("hwhwhw", "hwh")
    5
    >>> compute_max_string("frontsdakonsakdna", "front")
    5
    >>> compute_max_string("life", "life")
    4

    NEW DOCTESTS
    >>> compute_max_string("The Cat In The Hat", "the")
    0
    >>> compute_max_string("redgreenblue", "green")
    5
    >>> compute_max_string("It was a dark and gloomy night", "a")
    11
    """
    # YOUR CODE GOES HERE #
    if len(base) < len(pattern): 
        return 0 
    elif base.startswith(pattern):
        if base.endswith(pattern):
            return len(base)
        else:
            return compute_max_string(base[:-1], pattern) 
    else:
        if base.endswith(pattern):
             return compute_max_string(base[1:], pattern)
        else:
            return compute_max_string(base[1:-1], pattern)
