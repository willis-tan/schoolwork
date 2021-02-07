"""
DSC 20 Homework 02
Name: Willis
PID:  A14522499
"""

# Question 1
def convert_to_tuples(courses, instructors):
    """
    ##############################################################
    Given two lists: a list of courses and a list of instructors, this function
    will return a list tuples where each tuple has the course as the first
    element and its corresponding instructor as the second element.

    If no courses are provided, an empty list is returned.

    If a course at index k in the course list does not have a corresponding
    instructor in the instructor list, 'STAFF' will be the placeholder
    instructor name.
    ##############################################################

    Assumptions:
        len(courses) >= len(instructors).

    >>> convert_to_tuples(['DSC10', 'DSC20', 'DSC30', 'DSC40B',
    ... 'DSC80', 'DSC180A'], ['Justin Eldridge', 'Marina Langlois',
    ... 'Marina Langlois', 'Justin Eldridge', 'Marina Langlois',
    ... 'Aaron Fraenkel'])
    [('DSC10', 'Justin Eldridge'), ('DSC20', 'Marina Langlois'), \
('DSC30', 'Marina Langlois'), ('DSC40B', 'Justin Eldridge'), \
('DSC80', 'Marina Langlois'), ('DSC180A', 'Aaron Fraenkel')]

    >>> convert_to_tuples(['DSC102', 'DSC106', 'DSC100'],
    ... ['Arun Kumar', 'Thomas Powell'])
    [('DSC102', 'Arun Kumar'), ('DSC106', 'Thomas Powell'), \
('DSC100', 'STAFF')]

    >>> convert_to_tuples(['DSC90', 'DSC190'], [])
    [('DSC90', 'STAFF'), ('DSC190', 'STAFF')]

    NEW DOCTESTS
    >>> convert_to_tuples([], ['Gary Gillespie', 'Julian McAuley'])
    []
    >>> convert_to_tuples(['CSE 8A'], [])
    [('CSE 8A', 'STAFF')]
    >>> convert_to_tuples(['MATH 142A', 'MATH 109', 'MATH 20B'], [])
    [('MATH 142A', 'STAFF'), ('MATH 109', 'STAFF'), ('MATH 20B', 'STAFF')]
    """
    # YOUR CODE GOES HERE #
    if len(courses) == 0:
        return []

    output = []
    counter = 0
    for i in range(len(courses)):
        counter += 1
        if counter > len(instructors):
            output.append((courses[i], "STAFF"))
        else:
            output.append((courses[i], instructors[i]))
    return output


# Question 2
def convert_to_dict(tuples):
    """
    ##############################################################
    Takes a list of tuples where each tuple has the form (course, instructor).
    Returns a dictionary where the keys will be all unique instructors from the
    list of tuples, and the values will be a list of courses that each
    instructor teaches.

    The output will retain the relative order of keys and values that appear in
    the input list.
    ##############################################################

    Assumptions:
        there aren't duplicate instructor names or course codes.

    >>> convert_to_dict([('DSC10', 'Justin Eldridge'),
    ... ('DSC20', 'Marina Langlois'), ('DSC30', 'Marina Langlois'),
    ... ('DSC40B', 'Justin Eldridge'), ('DSC80', 'Marina Langlois'),
    ... ('DSC180A', 'Aaron Fraenkel')])
    {'Justin Eldridge': ['DSC10', 'DSC40B'], \
'Marina Langlois': ['DSC20', 'DSC30', 'DSC80'], 'Aaron Fraenkel': ['DSC180A']}

    >>> convert_to_dict([('DSC102', 'Arun Kumar'),
    ... ('DSC106', 'Thomas Powell'), ('DSC100', 'STAFF')])
    {'Arun Kumar': ['DSC102'], 'Thomas Powell': ['DSC106'], \
'STAFF': ['DSC100']}

    >>> convert_to_dict([('DSC90', 'STAFF'), ('DSC190', 'STAFF')])
    {'STAFF': ['DSC90', 'DSC190']}

    NEW DOCTESTS
    >>> convert_to_dict([])
    {}
    >>> convert_to_dict([('CSE 8A', 'STAFF')])
    {'STAFF': ['CSE 8A']}
    >>> convert_to_dict([('MATH 142A', 'STAFF'), ('MATH 109', 'STAFF'),
    ... ('MATH 20B', 'STAFF')])
    {'STAFF': ['MATH 142A', 'MATH 109', 'MATH 20B']}
    """
    # YOUR CODE GOES HERE #
    output = {}
    for course in tuples:
        course_name = course[0]
        instructor = course[1]

        if instructor in output:
            output[instructor].append(course_name)
        else:
            output[instructor] = [course_name]
    return output


# Question 3
def even_old_ops(string):
    """
    ##############################################################
    Characters of the string in the even indices are reversed with respect to
    order.

    Characters of the string in the odd indices that are originally uppercase
    will be lowercased. Those that are originally lowercase will be uppercased.
    Any other characters will replaced with "."

    Returns the transformed string, or an empty string if input is empty.
    ##############################################################

    >>> even_old_ops("Rand0mStr1NG")
    'NArDSM0Tn.Rg'
    >>> even_old_ops("d_s_c__20")
    '0._.c.s.d'
    >>> even_old_ops("0U1U2l3l4?5?6")
    '6u5u4L3L2.1.0'

    NEW DOCTESTS
    >>> even_old_ops("")
    ''
    >>> even_old_ops("......")
    '......'
    >>> even_old_ops("What Is The Result?")
    '?HlTsiR.eHT.sE UaTW'
    """
    # YOUR CODE GOES HERE #
    even_idx = []
    odd_idx = []
    for i in range(len(string)):
        if i % 2 == 0:
            even_idx.append(string[i])
        else:
            if (string[i].isalpha()):
                if (string[i].islower()):
                    odd_idx.append(string[i].upper())
                elif (string[i].isupper()):
                    odd_idx.append(string[i].lower())
            else:
                odd_idx.append(".")

    even_reversed = even_idx[::-1]

    output = []
    j = 0
    while (True):
        if j < len(even_reversed):
            output.append(even_reversed[j])
        if j < len(odd_idx):
            output.append(odd_idx[j])
        else:
            break
        j += 1
    return "".join(output)

# Question 4
def context_words(document, target_word, window_size):
    """
    ##############################################################
    Given a document string, target word, and window size, the function will
    return a list of tuples.

    Each tuple will follow the form (<target word>, <context word>), where
    context words are the words surrounding the target word.
    I.e, if window_size == 1, then the context words are the first word behind
    and the first word in front of the target word.

    If the target word appears multiple times in the document, then its context
    words will be found for all occurences.
    ##############################################################

    Assumptions:
        `document` is always a string where words are seperated by spaces.
        `document` string will only have uppercase or lowercase letters,
            hyphens (only in compound words), and spaces.
        `target_word` will always exist in the `document`.

    >>> test_doc = "fifty-two UNITS from lower-division courses " + \
    "AND sixty UNITS from upper-division courses"
    >>> context_words(test_doc, "lower-division", 2)
    [('lower-division', 'units'), ('lower-division', 'from'), \
('lower-division', 'courses'), ('lower-division', 'and')]
    >>> context_words(test_doc, "upper-division", 2)
    [('upper-division', 'units'), ('upper-division', 'from'), \
('upper-division', 'courses')]
    >>> context_words(test_doc, "units", 1)
    [('units', 'fifty-two'), ('units', 'from'), ('units', 'sixty'), \
('units', 'from')]

    NEW DOCTESTS
    >>> test_string = "The FitnessGram Pacer Test is a multistage aerobic \
capacity test that progressively gets more difficult as it continues"

    >>> context_words(test_string, "TEST", 2)
    [('test', 'fitnessgram'), ('test', 'pacer'), ('test', 'is'), \
('test', 'a'), ('test', 'aerobic'), ('test', 'capacity'), ('test', 'that'), \
('test', 'progressively')]
    >>> context_words(test_string, "the", 2)
    [('the', 'fitnessgram'), ('the', 'pacer')]
    >>> context_words(test_string, "continues", 2)
    [('continues', 'as'), ('continues', 'it')]
    """
    # YOUR CODE GOES HERE #
    target_word = target_word.lower()
    lowered = document.lower()
    words = lowered.split()
    target_idx = [i for i, word in enumerate(words) if word == target_word]

    output = []
    for idx in target_idx:
        for j in range(-min(window_size, idx), 0):
            output.append((target_word, words[idx + j]))
        for k in range(min(window_size, len(words) - 1 - idx)):
            output.append((target_word, words[idx + k + 1]))

    return output


# Question 5
def flip_matrix(matrix_path):
    """
    ##############################################################
    Given a file path to file a containing an N by M matrix, where each element
    is seperated by a space, this function will reverse the order of the rows
    and reverse the order of the elements of each row.

    The transformed matrix will be stored in a new file called 
    <filename>_flipped.txt, where <filename> is the filename of the given path.
    ##############################################################

    Assumptions:
        The matrix will be represented as lines of space-seperated integers.
        The matrix will be N x M, where N and M >= 1.

    >>> flip_matrix("testfiles/matrix1.txt")
    >>> with open("testfiles/matrix1_flipped.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    1 0 1 0 0
    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
    0 0 1 0 1
    >>> flip_matrix("testfiles/matrix2.txt")
    >>> with open("testfiles/matrix2_flipped.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    7 6 5 4 3
    6 5 4 3 2
    5 4 3 2 1
    >>> flip_matrix("testfiles/matrix3.txt")
    >>> with open("testfiles/matrix3_flipped.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    81 10051 99
    17 31 42
    1 770 90
    2 1 88
    96 51 52
    90 12 105

    NEW DOCTESTS
    >>> flip_matrix("testfiles/test_matrix1.txt")
    >>> with open("testfiles/test_matrix1_flipped.txt", "r") as testfile1:
    ...     print(testfile1.read().strip())
    1
    >>> flip_matrix("testfiles/test_matrix2.txt")
    >>> with open("testfiles/test_matrix2_flipped.txt", "r") as testfile2:
    ...     print(testfile2.read().strip())
    9 8 7 6 5 4 3 2 1
    >>> flip_matrix("testfiles/test_matrix3.txt")
    >>> with open("testfiles/test_matrix3_flipped.txt", "r") as testfile3:
    ...     print(testfile3.read().strip())
    9
    8
    7
    6
    5
    4
    3
    2
    1
    """
    # YOUR CODE GOES HERE #
    output_path = matrix_path[: matrix_path.find(".")] + "_flipped.txt"
    with open(matrix_path, "r") as in_file:
        with open(output_path, "w") as out_file:
            for line in reversed(in_file.readlines()):
                out_file.write(" ".join(line.split()[::-1]) + "\n")


# Question 6.1
def parse_timelog(timelog_path):
    """
    ##############################################################
    Given a path to timelog sorted in chronological order, this function will
    return a dictionary where its keys will be the tutors found in the timelog
    and their values will be a list of tuples indicating the day the tutor
    worked and the amount of hours worked on that day.
    ##############################################################

    Assumptions:
        The log will be sorted in chronological order.
        Each line of the time log will have name (str), date (str,
            MM-DD-YYYY), and minutes seperated by comma (",").
            For example: "Marina,09-30-2020,300".
        Each person will have only one entry per day.

    >>> parse_timelog("testfiles/timelog1.txt")
    {'Marina': [('09-30-2020', 300), ('10-01-2020', 300)], \
'Elvy': [('09-30-2020', 120), ('10-01-2020', 215)], \
'Yuxuan': [('09-30-2020', 185), ('10-01-2020', 90)]}
    >>> parse_timelog("testfiles/timelog2.txt")
    {'Colin': [('10-08-2020', 120), ('10-09-2020', 10), ('10-10-2020', 90), \
('10-11-2020', 30)], 'James': [('10-08-2020', 100), ('10-09-2020', 85)], \
'Simon': [('10-09-2020', 115)], 'Jerry': [('10-09-2020', 120)], \
'Sean': [('10-10-2020', 150)]}

    NEW DOCTESTS
    >>> parse_timelog("testfiles/test_timelog1.txt")
    {'Marvin': [('01-01-2020', 10)]}

    >>> parse_timelog("testfiles/test_timelog2.txt")
    {'Marvin': [('01-01-2020', 10), ('01-02-2020', 11), ('01-03-2020', 12), \
('01-04-2020', 13)]}

    >>> parse_timelog("testfiles/test_timelog3.txt")
    {'Marvin': [('01-01-2020', 10), ('01-02-2020', 10)], \
'Jack': [('01-01-2020', 60), ('01-21-2020', 120), ('01-22-2020', 120), \
('01-23-2020', 60)], \
'Jill': [('01-15-2020', 300)]}
    """
    # YOUR CODE GOES HERE #
    HOURS_IDX = 2

    tutor_timesheet = {}
    with open(timelog_path, "r") as f:
        for line in f.readlines():
            seperated = line.split(",")
            tutor = seperated[0]
            date = seperated[1]
            hours = seperated[HOURS_IDX]
            if tutor in tutor_timesheet:
                tutor_timesheet[tutor].append((date, int(hours)))
            else:
                tutor_timesheet[tutor] = [(date, int(hours))]
    return tutor_timesheet


# Question 6.2
def extract_extreme_time(data, is_max):
    """
    ##############################################################
    Given a dictionary created from parse_timelog(), this function will return
    a dictionary of each tutor's day that they worked the most or least.

    If is_max is true, then the day each tutor worked the most will be found.
    If is_max is false, then the day each tutor worked the least will be found.

    Keys will be each tutor found in the input dictionary.
    Values will be a single tuple in the form (<date>, <hours worked>).

    If the input data dictionary is empty, return an empty dictionary.
    ##############################################################

    Assumptions:
        When any comparison results a tie, keep the entry with earlier date.

    >>> data1 = parse_timelog("testfiles/timelog1.txt")
    >>> extract_extreme_time(data1, True)
    {'Marina': ('09-30-2020', 300), 'Elvy': ('10-01-2020', 215), \
'Yuxuan': ('09-30-2020', 185)}
    >>> extract_extreme_time(data1, False)
    {'Marina': ('09-30-2020', 300), 'Elvy': ('09-30-2020', 120), \
'Yuxuan': ('10-01-2020', 90)}
    >>> data2 = parse_timelog("testfiles/timelog2.txt")
    >>> extract_extreme_time(data2, True)
    {'Colin': ('10-08-2020', 120), 'James': ('10-08-2020', 100), \
'Simon': ('10-09-2020', 115), 'Jerry': ('10-09-2020', 120), \
'Sean': ('10-10-2020', 150)}
    >>> extract_extreme_time(data2, False)
    {'Colin': ('10-09-2020', 10), 'James': ('10-09-2020', 85), \
'Simon': ('10-09-2020', 115), 'Jerry': ('10-09-2020', 120), \
'Sean': ('10-10-2020', 150)}

    NEW DOCTESTS
    >>> extract_extreme_time({}, True)
    {}
    >>> extract_extreme_time(parse_timelog("testfiles/test_timelog1.txt"), \
True)
    {'Marvin': ('01-01-2020', 10)}

    >>> extract_extreme_time(parse_timelog("testfiles/test_timelog3.txt"), \
False)
    {'Marvin': ('01-01-2020', 10), 'Jack': ('01-01-2020', 60), \
'Jill': ('01-15-2020', 300)}
    """
    # YOUR CODE GOES HERE #
    output = {}
    for tutor in data:
        days = data[tutor]
        extrema = days[0]

        for i in range(1, len(days)):
            if is_max == True:
                if days[i][1] > extrema[1]:
                    extrema = days[i]
            elif is_max == False:
                if days[i][1] < extrema[1]:
                    extrema = days[i]

        output[tutor] = extrema 
    return output
