"""
DSC 20 Homework 05
Name: Willis Tan
PID:  A14522499
"""

# Question 1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function.
    Do not add new doctests for this function.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS #
    return [False, False, True, False, True, False, False, False, False, \
        False]


# Question 2
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function.
    Do not add new doctests for this function.

    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 7 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS #
    return [3, 5, 1, 2, 6, 4, 7, 4, 6, 5]


# Question 3
def advanced_search(data, min_elem, max_elem, min_total, max_total):
    """
    ##############################################################
    Given a dictionary and 4 numbers as arguments, return a list of names in
    the keys whose value list hold the following requirements

    For each value list:
    1. numeric values in the list are within the range min_elem and max_elem,
    both inclusive
    2. The sum of the list is between min_total and max_total, both inclusive.

    ##############################################################

    >>> data = {"Marina": [10, 9.2, 11.4, 17.5, 13.8], \
        "Elvy": [3.2, 8.6, 9.1, 1.0, 2.3, 6.6], \
        "Yuxuan": [14.41, 12.21, 10.01, 13, 11.1], \
        "Simon": [84.82, 91.96, 31.32], \
        "Sean": [66.0112, 88.8888, 45.6789], \
        "Colin": [44.1214, 55.5663, 77], \
        "Jerry": [10, 20, 30, 80]}
    >>> advanced_search(data, 10, 20, 0, 300)
    ['Yuxuan']
    >>> advanced_search(data, 40, 100, 150.5, 279.9)
    ['Sean', 'Colin']
    >>> advanced_search(data, 10, 80, 130, 150)
    ['Jerry']

    NEW DOCTESTS
    >>> data = {"Marina": [10, 9.2, 11.4, 17.5, 13.8], \
        "Elvy": [3.2, 8.6, -1.0, 2.3, 6.6, -7.6], \
        "Yuxuan": [14.41, 12.21, 10.01, 13, 11.1], \
        "Simon": [0, 0, 0], \
        "Sean": [-10, 3.14, 6.86, 10, 2.99, 0.01], \
        "Colin": [-13.0] \
        }
    >>> advanced_search(data, 0, 0, 13, 25)
    []
    >>> advanced_search(data, -10, 10, 13, 13)
    ['Sean']
    >>> advanced_search(data, -13, -13, -13, -13)
    ['Colin']
    """
    # YOUR CODE GOES HERE #
    vals = data.values()
    func = lambda x: min_elem <= x <= max_elem
    in_total_range = lambda y: (min_total <= sum(y) <= max_total)
    in_range = list(
        map(
            lambda lst: in_total_range(lst) and all(list(map(func, lst))), 
            vals
            )
        )

    names = list(data.keys())
    indices = list(filter(lambda i: in_range[i]==True, range(len(in_range))))
    
    return list(map(lambda idx: names[idx], indices))


# Question 4
def best_curve_function(scores, funcs):
    """
    ##############################################################
    Given a list of float scores between 0 and 100 inclusive, the function
    finds the best curve function from the funcs list such that the chosen
    function grants the highest cumulative increase in the scores list.

    Out of all the functions in the funcs list, only those with the following
    traits are considered:

    1. The function cannot decrease any score
    2. The function grants at most 5 more points

    If there are no suitable functions found, then the identity function will
    be returned.
    ##############################################################

    >>> best1 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 4.55, lambda score: score * 1.05, 105.0])
    >>> best1(100.0)
    104.55
    >>> best2 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 100, lambda score: score * 0.95, 103.5])
    >>> best2(95.5)
    95.5
    >>> best3 = best_curve_function([80.0, 90.0, 100.0], \
        [100.0, 103.5, False])
    >>> best3(91.0)
    91.0

    NEW DOCTESTS
    >>> test1 = best_curve_function([0.0, 76.7, 33.33, 100.0], \
        [lambda score: score + 5.01, lambda score: (score * 2)**0.5])
    >>> test1(50.0)
    50.0

    >>> test2 = best_curve_function([0.0, 0.9, 0.04, 0.49], \
        [lambda score: (score ** 0.5), lambda score: (score * 3)])
    >>> test2(100.0)
    300.0

    >>> test3 = best_curve_function([0.0, 0.9, 0.04, 0.49], \
        [lambda score: (score ** 0.5), lambda score: (score - 1)])
    >>> test3(100.0)
    10.0
    """
    # YOUR CODE GOES HERE #
    MAX_SCORE = 100
    MAX_INC = 5

    assert isinstance(scores, list) and len(scores) > 0
    assert all(isinstance(x, float) and (0 <= x <= MAX_SCORE) for x in scores)

    # Step 1
    are_funcs = list(filter(callable, funcs))

    '''
    Given a curve function, this inner function will determine whether or not a
    given curve function is suitable. I.e, cannot decrease scores and grants no
    more than 5 extra points. 
    '''
    def good_func(func):
        new_scores = list(map(func, scores))
        new_then_original = list(zip(new_scores, scores))

        reqs = lambda pair: pair[0] >= pair[1] and \
            (pair[0] <= (pair[1] + MAX_INC))
        return all(map(reqs, new_then_original))

    valid_funcs = list(filter(good_func, are_funcs))

    # Step 2
    total_improvement = 0
    out = lambda x: x
    for f in valid_funcs:
        new_scores = list(map(f, scores))

        metric = 0
        for i in range(len(scores)):
            metric += (new_scores[i] - scores[i])
        if metric > total_improvement:
            total_improvement = metric
            out = f

    return out
