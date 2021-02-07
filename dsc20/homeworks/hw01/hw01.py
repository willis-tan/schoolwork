# DSC 20 Homework 01
# Name: Willis Tan
# PID:  A14522499

# Question 1
def older_tutor(first_name, first_age, second_name, second_age):
    """
    A function that returns the name of the older tutor given their names (as
    strings) and ages (as positive integers). If they happen to be of the same
    age, return a string: 'Same Age'.

    >>> older_tutor("Aaron", 22, "James", 21)
    'Aaron'
    >>> older_tutor("Elvy", 18, "Yuxuan", 20)
    'Yuxuan'
    >>> older_tutor("Simon", 999, "Sean", 999)
    'Same Age'
    
    NEW DOCTESTS
    >>> older_tutor("", 33, "o7", 21)
    ''
    >>> older_tutor("Bond", 99, "Bond", 100)
    'Bond'
    >>> older_tutor("Jim", 10, "Jim", 10)
    'Same Age'
    """
    
    if first_age > second_age:
        return first_name
    elif first_age < second_age:
        return second_name
    else:
        return "Same Age"


# Question 2
def older_tutor_year_month(f_name, f_year, f_month, s_name, s_year, s_month):
    """
    A function that that returns the name of the older tutor, given their
    names (as strings), years (as positive integers), and months (0 to 11).
    If they happen to be the same age return a string: 'Same Age'.

    You can reuse the function from the first question when needed.

    >>> older_tutor_year_month("Aaron", 22, 10, "James", 22, 5)
    'Aaron'
    >>> older_tutor_year_month("Elvy", 18, 11, "Yuxuan", 18, 11)
    'Same Age'
    >>> older_tutor_year_month("Simon", 10, 11, "Sean", 30, 3)
    'Sean'
    
    NEW DOCTESTS
    >>> older_tutor_year_month("Jim", 11, 11, "Jim", 11, 11)
    'Same Age'
    >>> older_tutor_year_month("Mick", 57, 5, "Mick", 57, 7)
    'Mick'
    >>> older_tutor_year_month("Tim", 39, 0, "Todd", 39, 1)
    'Todd'
    """
    
    if f_year < s_year:
        return s_name
    elif f_year > s_year:
        return f_year
    else:
        if f_month > s_month:
            return f_name
        elif f_month < s_month:
            return s_name
        else:
            return "Same Age"


# Question 3
def message(name, dow, time):
    """
    A function that takes in (name, day of the week, time) and returns
    Sharmi's invitation to her discussion session. Check the doctest
    for the output string format.

    Note:
        <BLANKLINE> denotes a blank line in doctest.
        DO NOT append this token to the returned string.

    >>> print(message("Marina", "Friday", "4:00 PM"))
    Dear Marina,
    Please join our discussion on Friday at 4:00 PM.
    <BLANKLINE>
    Sharmi
    
    NEW DOCTESTS
    >>> print(message("Willis", "Monday", "4:00 - 6:00 PM"))
    Dear Willis,
    Please join our discussion on Monday at 4:00 - 6:00 PM.
    <BLANKLINE>
    Sharmi
    >>> print(message("Students", "Tuesday and Thursday", "9 AM PST"))
    Dear Students,
    Please join our discussion on Tuesday and Thursday at 9 AM PST.
    <BLANKLINE>
    Sharmi
    >>> print(message("CAT 125R", "Wednesday", "1:30 PM"))
    Dear CAT 125R,
    Please join our discussion on Wednesday at 1:30 PM.
    <BLANKLINE>
    Sharmi
    """
    
    template = "Dear {0},\nPlease join our discussion on {1} at {2}.\n\nSharmi"
    return template.format(name, dow, time)


# Question 4
def larger_room(
    first_name,
    first_room_length,
    first_room_width,
    second_name,
    second_room_length,
    second_room_width,
):
    """
    A function that returns the name of the tutor living in a larger room,
    given their names (as strings), and their room dimensions (height and
    width as positive integers). If they happen to have the same room area,
    return a string: "Same Area".

    You may assume that their rooms are rectangular.

    >>> larger_room("Aaron", 22, 5, "James", 22, 10)
    'James'
    >>> larger_room("Elvy", 18, 11, "Yuxuan", 20, 3)
    'Elvy'
    >>> larger_room("Simon", 30, 3, "Sean", 2, 45)
    'Same Area'
    
    NEW DOCTESTS
    >>> larger_room("Billy", 100, 70, "Mays", 1, 6999)
    'Billy'
    >>> larger_room("Mick", 5, 5, "Gordon", 5, 5)
    'Same Area'
    >>> larger_room("John", 1, 1, "Cena", 1, 2)
    'Cena'
    """

    first_room_area = first_room_length * first_room_width
    second_room_area = second_room_length * second_room_width

    if first_room_area > second_room_area:
        return first_name
    elif first_room_area < second_room_area:
        return second_name
    else:
        return "Same Area"


# Question 5
def larger_multidim_room(
    first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room,
    given their names (as strings), and their room dimensions (as a list of
    positive integers). If they happen to have the same room volume,
    return a string: "Same Volume".

    You may assume two rooms have the same number of dimensions.

    >>> larger_multidim_room("Aaron", [22, 5, 7, 11], "James", [10, 11, 2, 9])
    'Aaron'
    >>> larger_multidim_room("Elvy", [11, 8, 1], "Yuxuan", [3, 5, 20])
    'Yuxuan'
    >>> larger_multidim_room("Simon", [20, 9], "Sean", [18, 10])
    'Same Volume'
    
    NEW DOCTESTS
    >>> larger_multidim_room("Alex", [1, 1, 1], "Alex", [1, 1, 1])
    'Same Volume'
    >>> larger_multidim_room("Boba", [1, 2, 4, 8], "Django", [1, 3, 9, 27])
    'Django'
    >>> larger_multidim_room("Dean", [20], "Bean", [18])
    'Dean'
    """
    
    first_room_vol = 1
    second_room_vol = 1

    for i in first_room_dims:
        first_room_vol *= i
    for j in second_room_dims:
        second_room_vol *= j

    if first_room_vol > second_room_vol:
        return first_name
    elif first_room_vol < second_room_vol:
        return second_name
    else:
        return "Same Volume"


# Question 6
def larger_room_subspace(
    ndim, first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room with
    larger subspace (calculated using only the first `ndim` dimensions), given
    their names (as strings), and their room dimensions (as a list of positive
    integers). If they happen to have the same room volume, return a string:
    "Same Volume".

    You may assume two rooms have the same number of dimensions, and `ndim`
    won't exceed the number of dimensions of both rooms.

    >>> larger_room_subspace(2, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'Same Volume'
    >>> larger_room_subspace(3, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'James'

    >>> larger_room_subspace(5, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'Aaron'
    
    NEW DOCTESTS
    >>> larger_room_subspace(5, "Cat", [1, 1, 1, 1, 1],
    ...                         "Dog", [1, 1, 1, 1, 1])
    'Same Volume'
    >>> larger_room_subspace(3, "Otto", [1, 1, 10, 1, 1],
    ...                         "Bismarck", [1, 1, 1, 1, 10])
    'Otto'
    >>> larger_room_subspace(1, "Brick", [2, 4, 6, 8, 10],
    ...                         "Roland", [3, 5, 7, 9, 11])
    'Roland'
    """
    # YOUR CODE GOES HERE #
    first_room_volume = 1
    second_room_volume = 1

    for i in range(ndim):
        first_room_volume *= first_room_dims[i]
        second_room_volume *= second_room_dims[i]
    
    if first_room_volume > second_room_volume:
        return first_name
    elif first_room_volume < second_room_volume:
        return second_name
    else:
        return "Same Volume"


# Question 7
def larger_room_subspace_unbounded(
    ndim, first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room with
    larger subspace (calculated using only the first `ndim` dimensions), given
    their names (as strings), and their room dimensions (as a list of positive
    integers). If they happen to have the same room volume, return a string:
    "Same Volume".

    If the given dimensions `ndim` exceeds the number of dimensions of both
    rooms, you should apply the following procedure to each room:
        (1) Find the dimensions with maximum and minimum length
        (2) Take the square root of the product of the max and min found
        (3) Truncate this number to only keep the 3 digits after the decimal
        point
    Then, compare the truncated numbers of two rooms, and return the name of
    the tutor associated with a larger truncated number, or "Same Volume"
    if two numbers are equal.

    You may assume two rooms have the same number of dimensions.

    >>> larger_room_subspace_unbounded(10, "Yuxuan", [2, 8, 6, 8, 9],
    ...                                    "James", [4, 1, 18, 15, 6])
    'Same Volume'
    >>> larger_room_subspace_unbounded(10, "Aaron", [2, 4, 6, 7, 8],
    ...                                    "James", [4, 2, 8, 10, 3])
    'James'
    >>> larger_room_subspace_unbounded(10, "Jerry", [9, 7, 1, 2, 11],
    ...                                    "Colin", [8, 5, 8, 3, 12])
    'Jerry'

    NEW DOCTESTS
    >>> larger_room_subspace_unbounded(3, "Jerry", [9, 7, 1, 2, 11],
    ...                                    "Colin", [8, 5, 8, 3, 12])
    'Colin'
    >>> larger_room_subspace_unbounded(1, "Jerry", [9, 7, 1, 2, 11],
    ...                                    "Colin", [8, 5, 8, 3, 12])
    'Jerry'
    >>> larger_room_subspace_unbounded(10, "Jerry", [1, 1, 1, 1, 11],
    ...                                    "Colin", [1, 1, 1, 1, 16])
    'Jerry'
    """
    
    SQUARE_ROOT = 0.5
    TEN_THOUSANDTHS_PLACE = 4

    num_dimensions = len(first_room_dims)
    
    if ndim <= num_dimensions:
        return larger_room_subspace(
            ndim, first_name, first_room_dims, second_name, second_room_dims
        )
    else:
        first_max = max(first_room_dims)
        second_max = max(second_room_dims)
        first_min = min(first_room_dims)
        second_min = min(second_room_dims)
        
        first_room_root = str((first_max * first_min) ** SQUARE_ROOT)
        second_room_root = str((second_max * second_min) ** SQUARE_ROOT)

        first_decimal_idx = first_room_root.find(".")
        second_decimal_idx = second_room_root.find(".")

        first_room_num = int(first_room_root[
            first_decimal_idx + 1: first_decimal_idx + TEN_THOUSANDTHS_PLACE
            ])
        second_room_num = int(second_room_root[
            second_decimal_idx + 1: second_decimal_idx + TEN_THOUSANDTHS_PLACE
            ])
        
        if first_room_num < second_room_num:
            return second_name
        elif first_room_num > second_room_num:
            return first_name
        else:
            return "Same Volume"
    


# Question 8
def odd_even_list(names):
    """
    A function that returns a list, where each name in the names list is 
    replaced with the string "Even" if the name has even length, or "Odd" 
    otherwise. If the names list is empty, return a list with the string 
    "Empty list was given" in it.

    >>> odd_even_list(["Marina", "Elvy", "James", "Sharmi"])
    ['Even', 'Even', 'Odd', 'Even']
    >>> odd_even_list(["Yuxuan", "Simon", "Sean"])
    ['Even', 'Odd', 'Even']
    >>> odd_even_list([])
    ['Empty list was given']

    NEW DOCTESTS
    >>> odd_even_list(["", "", " ", " "])
    ['Even', 'Even', 'Odd', 'Odd']
    >>> odd_even_list(["Dr. Octopus", "Spider Man", "Electro"])
    ['Odd', 'Even', 'Odd']
    >>> odd_even_list(["a", "list", "of", "words"])
    ['Odd', 'Even', 'Even', 'Odd']
    """
    
    if len(names) == 0:
        return ["Empty list was given"]

    EVEN_CHECK = 2

    for i in range(len(names)):
        if (len(names[i]) % EVEN_CHECK == 0):
            names[i] = "Even"
        else:
            names[i] = "Odd"
    return names


# Question 9
def is_james_more_than_aaron(names):
    """
    A function that returns whether the name 'James' occurs more often than
    the name 'Aaron' in the input list of names. Return True if the above
    statement is true.

    >>> is_james_more_than_aaron(["James", "Aaron", "James"])
    True
    >>> is_james_more_than_aaron(["Aaron", "Aaron"])
    False
    >>> is_james_more_than_aaron(["Aaron", "Marina", "Yuxuan", "James"])
    False

    NEW DOCTESTS
    >>> is_james_more_than_aaron([])
    False
    >>> is_james_more_than_aaron(["Aaron", "aaron", "AARON", "James", "James"])
    True
    >>> is_james_more_than_aaron(["aaron", "aaron", "james", "james"])
    False
    """
    james_counter = 0
    aaron_counter = 0
    for name in names:
        if name == "James":
            james_counter += 1
        elif name == "Aaron":
            aaron_counter += 1
    return james_counter > aaron_counter


# Question 10
def string_sum(lst):
    """
    A function that calculates the sum of all integers in the input list. All
    integers in the input list are given in string format, and the returned
    sum should also be a string.

    >>> string_sum(["1", "2", "3"])
    '6'
    >>> string_sum(["111", "205", "377"])
    '693'
    >>> string_sum(["777", "-999"])
    '-222'

    NEW DOCTESTS
    >>> string_sum(["-0", "0", "1"])
    '1'
    >>> string_sum([])
    '0'
    >>> string_sum(["100", " -99 ", "-0"])
    '1'
    """
    # YOUR CODE GOES HERE #
    summation = 0
    for num in lst:
        summation += int(num)
    return str(summation)
