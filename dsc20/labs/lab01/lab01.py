# DSC 20 Lab 01
# Name: Willis Tan
# PID:  A14522499

# Question 1
def password_1(first_name, last_name):
    """
    Return a password string constructed by concatenating the first 2 
    characters of the first name and the last 2 characters of the last name, 
    repeating this pattern twice, and appending the full last name at the end. 
    If either name is shorter than 2 characters, concatenate the names and 
    repeat this pattern three times.

    >>> password_1("Marina", "Langlois")
    'MaisMaisLanglois'
    >>> password_1("Donald", "Trump")
    'DompDompTrump'
    >>> password_1("Marina", "")
    'MarinaMarinaMarina'
    >>> password_1("","")
    ''
    >>> password_1("J", "Yo")
    'JYoJYoJYo'
    >>> password_1(" ", " ")
    '      '

    NEW DOCTESTS
    >>> password_1(" h ", " i ")
    ' hi  hi  i '
    >>> password_1(" _jim_ ", "_")
    ' _jim_ _ _jim_ _ _jim_ _'
    >>> password_1("_a ", "5 _ t")
    '_a t_a t5 _ t'
    """
    CHARACTER_LIMITER = 2
    TWO_REPEATS = 2
    THREE_REPEATS = 3

    if (len(first_name) <= 1) or (len(last_name) <= 1):
        password = THREE_REPEATS * (first_name + last_name)
    else:
        password = TWO_REPEATS * (
                        first_name[:CHARACTER_LIMITER]
                        + last_name[-CHARACTER_LIMITER:]
                    ) + last_name

    return password


# Question 2
def password_2(param1, param2, param3):
    """
    Return a password string constructed with the following rules:
        (1) If there are only 0 or 1 numeric among 3 parameters, concatenate 
        the string form of all parameters directly.
        (2) If there are 2 numeric parameters, calculate the sum of 2 numeric 
        values if they are both int, or calculate the product of them and round 
        to 2 decimal places if any of them is float. Finally, append this 
        sum/product to the string parameter.

    You may assume that there will be at least 1 string parameter.

    >>> password_2("Marina", "Langlois", "20")
    'MarinaLanglois20'
    >>> password_2("Marina", "Langlois", 20)
    'MarinaLanglois20'
    >>> password_2("Elvy", True, 20)
    'ElvyTrue20'
    >>> password_2(True, 20, "Elvy")
    'True20Elvy'
    >>> password_2(20, 40, "Elvy")
    'Elvy60'
    >>> password_2(20, "Elvy", 3)
    'Elvy23'
    >>> password_2(2, 3.333, "Elvy")
    'Elvy6.67'

    NEW DOCTESTS
    >>> password_2(0.0, "X", 72)
    'X0.00'
    >>> password_2("X ", "", " Y")
    'X  Y'
    >>> password_2(1, "234", " is bad password")
    '1234 is bad password'
    """

    MAX_NUMERIC_ARGS = 2

    params = [
        param1,
        param2,
        param3
    ]
    
    num_numeric = 0
    num_floats = 0
    summation = 0
    product = 1
    for i in params:
        if type(i) is int:
            num_numeric += 1
            summation += i
            product *= i
        elif type(i) is float:
            num_numeric += 1
            num_floats += 1
            product *= i
        else:
            string_param = str(i)
        
    if num_numeric <= 1:
        return str(param1) + str(param2) + str(param3)
    elif num_numeric == MAX_NUMERIC_ARGS:
        if num_floats >= 1:
            return string_param + "{:0.2f}".format(product)
        else:
            return string_param + str(summation)


# Question 3
def access(nickname, permission_lvl, super_access):
    """
    Return a string that shows the permissions associated with the person with
    given nickname. The possible permission levels are 0 (read), 1 (read and 
    write), and 2 (read, write and invite). If super_access is set to True, 
    this person ignores the permission level and has the full access. See the 
    doctest for the output string format.

    You may assume that nickname is a string, permission_lvl is in (0, 1, 2),
    and super_access is a boolean value.

    >>> access("Marina", 2, True)
    'Marina, you have full access'
    >>> access("Sean", 1, True)
    'Sean, you have full access'
    >>> access("Jerry", 0, True)
    'Jerry, you have full access'
    >>> access("Elvy", 2, False)
    'Elvy, you are authorized to: read, write and invite'
    >>> access("Yuxuan", 1, False)
    'Yuxuan, you are authorized to: read and write'
    >>> access("Simon", 0, False)
    'Simon, you are authorized to: read'

    NEW DOCTESTS
    >>> access("", 0, False)
    ', you are authorized to: read'
    >>> access("user#1234", 0, True)
    'user#1234, you have full access'
    >>> access(" ", 1, False)
    ' , you are authorized to: read and write'
    """

    MAX_PERMISSION_LVL = 2

    if super_access:
        return nickname + ", you have full access"
    
    if permission_lvl == 0:
        message = ", you are authorized to: read"
    elif permission_lvl == 1:
        message = ", you are authorized to: read and write"
    elif permission_lvl == MAX_PERMISSION_LVL:
        message = ", you are authorized to: read, write and invite"
    return nickname + message


# Question 4
def repeats(passwords, to_search, num_of_repeats):
    """
    A function that takes in a list of passwords (as strings), a password that 
    needs to be checked (as a string), and an integer that represents the 
    number of repetitions. If the given password occurs given number of times, 
    return True, else return False.

    >>> repeats(["ma48", "ma28", "ma48"], "ma48", 2)
    True
    >>> repeats(["ma48", "ma28", "ma48"], "ma48", 3)
    False
    >>> repeats(["ma48", "ma28", "ma48", "ma28", "ma48"], "ma38", 2)
    False
    >>> repeats(["ma48", "ma28", "ma48", "ma38"], "ma48", 1)
    False

    NEW DOCTESTS
    >>> repeats([], "ma48", 2)
    False
    >>> repeats(["ma20", "ma28", "ma41"], "ma48", 0)
    True
    >>> repeats(["ma48", "ma28", "ma48"], "", 1)
    False
    """
    num_occurences = 0
    for password in passwords:
        if password == to_search:
            num_occurences += 1

    return num_occurences == num_of_repeats
