# DSC 20 Lab 00
# Name: Willis Tan
# PID:  A14522499

def name_sum(firstName, lastName):
    """
    Write a Python program to sum up the lengths of two given names. 
    However, if the sum is strictly greater than 15, return only the 
    length of the firstName. If the sum is less than 10, return my 
    name as a string: "Marina".

    >>> name_sum("Marina", "Langlois")
    14
    >>> name_sum("Elvy", "Chen")
    'Marina'
    >>> name_sum("Kiefer", "Sutherland")
    6
    """
    length_fname = len(firstName)
    length_lname = len(lastName)
    length_both_names =  length_fname + length_lname

    if length_both_names > 15:
        return length_fname
    elif length_both_names < 10:
        return "Marina"
    else:
        return length_both_names
