"""
DSC 20 Homework 09
Name: Willis Tan
PID:  A14522499
"""


# Question 1
def check_inputs(input1, input2):
    """
    Function to check the correctness of input1 and input2.

    1. input1 must be a list
    2. all elements of input1 must be numeric OR input1 can be empty
        - If a nonnumeric element is found, raise a TypeError and identify the
        index of the first nonnumeric element
    3. input2 must be numeric
    4. input2 must be in input1

    If all 4 checks are met, return 'Input validated'

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'

    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type

    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric

    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type


    NEW DOCTESTS
    >>> check_inputs([1.0, 2.0, 3.0, 4.0], 4)
    'Input validated'

    >>> check_inputs(['1.0', 2.0, 3.0, 4.0], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 0 is not numeric

    >>> check_inputs([1.0, 2.0, 3.0, 4.0], '4')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type

    >>> check_inputs([1.0, 2.0, True, 4.0], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    """
    if not isinstance(input1, list):
        raise TypeError('input1 is not the correct type')
    for i in range(len(input1)):
        if not(type(input1[i]) == int or type(input1[i]) == float):
            raise TypeError('The element at index {} is not numeric'.format(i))
    if not(type(input2) == int or type(input2) == float):
        raise TypeError('input2 is not the correct type')
    if input2 not in input1:
        raise TypeError('input2 not in input1')
    return 'Input validated'


# Question 2
def load_file(filename):
    """
    Function to check if the given filename is valid. A filename is valid if:

    1. it is a string
    2. the file with the filename can be opened (already exists)
    3. the associated file cannot be empty (has at least 1 character)

    If all checks pass, return the number of words in the file.

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    >>> load_file('files/ten_words.txt')
    10

    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty

    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist


    NEW DOCTESTS
    >>> load_file('U21PEM6""B35A16sd hn')
    Traceback (most recent call last):
    ...
    FileNotFoundError: U21PEM6""B35A16sd hn does not exist
    >>> load_file('files/five_words.txt')
    5
    >>> load_file('files/five_mixed_type_words.txt')
    5
    """
    if not(isinstance(filename, str)):
        raise TypeError('filename is not a string')

    try:
        with open(filename, 'r') as f:
            text = f.read()
    except:
        raise FileNotFoundError(filename + ' does not exist')
    else:
        length = len(text.split())
        if length == 0:
            raise ValueError('File is empty')
        return length


# Question 3
def q3_doctests():
    """
    Q3 doctests go here.

    >>> h = Nonmetal("H")
    >>> h
    Nonmetal("H")
    >>> print(h)
    Nonmetal name: H, atomic number: 8, period: 2, group: 2
    >>> h.get_mass()
    66

    >>> f = Metal("F")
    >>> f
    Metal("F")
    >>> print(f)
    Metal name: F, atomic number: 6, period: 1, group: 6
    >>> f.get_mass()
    78

    >>> f == h
    False
    >>> f != h
    True
    >>> f > h
    True
    >>> f < h
    False

    >>> water = Compound("H2O1")
    >>> water
    Compound("H2O1")
    >>> print(water)
    H2O1
    >>> water.elements
    {'H': 2, 'O': 1}
    >>> water.get_compound_mass()
    255

    >>> yummy_metal = Compound("U1")
    >>> dsc2 = Compound("D2S2C2")
    >>> dsc3 = Compound("D3S3C3")
    >>> cse = Compound("C7S8E9")
    >>> lava = Compound("H3O4")
    >>> obsidian = Compound("H5O5")
    >>> smelly_gas = Compound("H2")

    >>> water == yummy_metal
    True
    >>> water <= yummy_metal
    True
    >>> water > dsc2
    False

    >>> dsc2 + dsc3
    Compound("C5D5S5")
    >>> water - smelly_gas
    Compound("O1")
    >>> dsc2 + cse
    Traceback (most recent call last):
    ...
    ValueError
    >>> water - lava
    Traceback (most recent call last):
    ...
    ValueError
    >>> water + lava == obsidian
    True
    """
    return


LIST_METAL = "FKLPQRUVWXZ"
SET_METAL = set([metal for metal in LIST_METAL])

MIN_ASCII = 65
MAX_ASCII = 90
class Element:
    """
    The parent class Element serves as a blueprint for the Metal and Nonmetal
    classes.

    Element names range from A to Z inclusive.
    Atomic numbers range from 1 to 26 inclusive.
    Group numbers range from 1 to 6 and period numbers range from 1 to 5, both
    inclusive.
    """

    def __init__(self, name):
        """
        Constructor of Element

        Input validation is required

        Parameter:
        name (str): a single uppercase character from 'A' to 'Z' that
                    represents the name of the element
        """
        # YOUR CODE GOES HERE #
        OFFSET = 64
        DIVISOR = 6

        if (len(name) > 1) or not(MIN_ASCII <= ord(name) <= MAX_ASCII):
            raise ValueError('invalid argument')
        self.name = name
        self.atomic_num = ord(name) - OFFSET

        group = self.atomic_num % DIVISOR
        if group != 0:
            self.group = group
        else:
            self.group = DIVISOR
        ceiling = lambda a: -(-a // DIVISOR)
        self.period = ceiling(self.atomic_num)


    def get_mass(self):
        """
        Returns atomic mass of this element

        This method is a placeholder to avoid style check errors in some
        editors or tools. You will overwrite this method in the subclasses.
        """
        # DO NOT MODIFY #
        raise NotImplementedError("must be implemented in the subclasses")

    def __eq__(self, other_elem):
        """
        Returns True when two Elements are equal.
        Equality is determined by their atomic mass
        """
        # YOUR CODE GOES HERE #
        return self.get_mass() == other_elem.get_mass()

    def __ne__(self, other_elem):
        """ Returns True when two Elements are not equal """
        # YOUR CODE GOES HERE #
        return self.get_mass() != other_elem.get_mass()

    def __gt__(self, other_elem):
        """ Returns True when this Element is greater than the other """
        # YOUR CODE GOES HERE #
        return self.get_mass() > other_elem.get_mass()

    def __ge__(self, other_elem):
        """
        Returns True when this Element is greater than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_mass() >= other_elem.get_mass()

    def __lt__(self, other_elem):
        """ Returns True when this Element is less than the other """
        # YOUR CODE GOES HERE #
        return self.get_mass() < other_elem.get_mass()

    def __le__(self, other_elem):
        """
        Returns True when this Element is less than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_mass() <= other_elem.get_mass()

    def __repr__(self):
        """ Returns object representation of this Element """
        # uncomment the following code
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form


class Nonmetal(Element):
    """
    Elements that are nonmetals are initialized from the Nonmetal class.

    The mass of nonmetals is determined by:
        8 * atomic number + period number
    """

    def get_mass(self):
        NONMETAL_SCALAR = 8
        """ Returns atomic mass of this Nonmetal element """
        # YOUR CODE GOES HERE #
        return NONMETAL_SCALAR * self.atomic_num + self.period

    def __str__(self):
        """ Returns string representation of this Nonmetal element """
        # uncomment the following code
        str_form = \
            "Nonmetal name: {}, atomic number: {}, period: {}, group: {}"
        return str_form.format(self.name, self.atomic_num, self.period, \
            self.group)


class Metal(Element):
    """
    Elements that are metals are initialized from the Metal class.

    The mass of nonmetals is determined by:
        12 * atomic number + period number
    """

    def get_mass(self):
        METAL_SCALAR = 12
        """ Returns atomic mass of this Metal element """
        # YOUR CODE GOES HERE #
        return METAL_SCALAR * self.atomic_num + self.group

    def __str__(self):
        """ Returns string representation of this Metal element """
        # uncomment the following code
        str_form = "Metal name: {}, atomic number: {}, period: {}, group: {}"
        return str_form.format(self.name, self.atomic_num, self.period, \
            self.group)

EVEN = 2
MIN_LENGTH = 2
MAX_ELEMENTS = 9
class Compound:
    """
    The Compound class represents combination of elements. Compounds are one or
    more elements combined together. Compounds can only have 1 to 9 (inclusive)
    atoms of each element. Compound names are sorted by element names are
    unique, an element cannot show up twice in a compound name.
    """

    def __init__(self, name):
        """
        Constructor of Compound

        Input validation is required

        Parameter:
        name (str): a string that represents the name of the compound
        """
        # YOUR CODE GOES HERE #
        # check if there is at least one element
        if len(name) < MIN_LENGTH or len(name) % EVEN == 1:
            raise ValueError('invalid argument')
        letter = '@'
        element_dict = dict()
        for i in range(len(name)):
            char = name[i]
            # check even indices for A-Z
            if i % EVEN == 0:
                if not(MIN_ASCII <= ord(char) <= MAX_ASCII):
                    raise ValueError('invalid argument')
                letter = char
                # handle duplicate element
                if letter in element_dict:
                    raise ValueError('invalid argument')
                element_dict[letter] = 0
            # check odd indices for 1-9
            elif i % EVEN == 1:
                number = int(char)
                if not(1 <= number <= MAX_ELEMENTS):
                    raise ValueError('invalid argument')
                element_dict[letter] = number
        
        self.name = name
        self.elements = element_dict

        mass = 0
        for elem in element_dict:
            if elem in SET_METAL:
                mass += (element_dict[elem] * Metal(elem).get_mass())
            else:
                mass += (element_dict[elem] * Nonmetal(elem).get_mass())
        self.compound_mass = mass

    def get_compound_mass(self):
        """ A simple getter of compound_mass """
        # YOUR CODE GOES HERE #
        return self.compound_mass

    def __eq__(self, other_comp):
        """
        Returns True when two Compounds are equal.
        Equality is determined by their compound mass
        """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() == other_comp.get_compound_mass()

    def __ne__(self, other_comp):
        """ Returns True when two Compounds are not equal """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() != other_comp.get_compound_mass()

    def __gt__(self, other_comp):
        """ Returns True when this Compound is greater than the other """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() > other_comp.get_compound_mass()

    def __ge__(self, other_comp):
        """
        Returns True when this Compound is greater than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() >= other_comp.get_compound_mass()

    def __lt__(self, other_comp):
        """ Returns True when this Compound is less than the other """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() < other_comp.get_compound_mass()

    def __le__(self, other_comp):
        """
        Returns True when this Compound is less than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() <= other_comp.get_compound_mass()

    def __add__(self, other_comp):
        """
        Synthesize a new Compound by adding this Compound with another

        Exception:
        ValueError will be raised if the product is invalid
        """
        # YOUR CODE GOES HERE #
        this = self.elements
        other = other_comp.elements
        add_elem = lambda x: this.get(x, 0) + other.get(x, 0)
        summed = dict()
        for x in set(this).union(other):
            val = add_elem(x)
            if val > MAX_ELEMENTS:
                raise ValueError()
            else:
                summed[x] = val

        new_name = ''
        keys = sorted(summed.keys())
        for k in keys:
            new_name += (k + str(summed[k]))

        return Compound(new_name)

    def __sub__(self, other_comp):
        """
        Decompose this Compound by subtracting another from it. A new product
        is returned after decomposition

        Exception:
        ValueError will be raised if the product is invalid
        """
        # YOUR CODE GOES HERE #
        this = self.elements
        other = other_comp.elements
        minus_elem = lambda x: this.get(x, 0) - other.get(x, 0)
        summed = dict()
        for x in set(this).union(other):
            val = minus_elem(x)
            if val < 0:
                raise ValueError()
            elif val == 0:
                continue
            else:
                summed[x] = val

        new_name = ''
        keys = sorted(summed.keys())
        for k in keys:
            new_name += (k + str(summed[k]))

        return Compound(new_name) 

    def __str__(self):
        """ Returns string representation of this Compound """
        # YOUR CODE GOES HERE #
        return self.name

    def __repr__(self):
        """ Returns object representation of this Compound """
        # uncomment the following code
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form
