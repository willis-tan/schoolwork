"""
DSC 20 Lab 03
Name: Willis Tan
PID:  A14522499
"""


# Question 1
def is_fair_game(*player_ranks):
    """
    Judge whether the game is fair given player ranks (as int). A game is
    fair if players can be divided into two teams of equal size, and the
    rank difference between the highest and lowest is less than or equal to 5.

    >>> is_fair_game(50, 49, 52, 48)
    True
    >>> is_fair_game(6, 7, 5, 4, 6)
    False
    >>> is_fair_game(230, 231, 232, 220)
    False
    """

    if (len(player_ranks) % 2 != 0) or (len(player_ranks) == 0):
        return False

    return (max(player_ranks) - min(player_ranks) <= 5)


# Question 2
def matchmaking(**games):
    """
    Simulate a matchmaking system that runs several games and judge
    whether they are fair games. Return a dictionary that has game name
    as key, and the judge result as value. For each game, if it is fair,
    return all players' ranks that are higher than the game average;
    otherwise, return 'not a fair game'.

    >>> matchmaking(game_1=[50, 49, 51, 52], game_2=[71, 73, 71, 71],
    ... game_3=[18, 23, 22, 18])
    {'game_1': [51, 52], 'game_2': [73], 'game_3': [23, 22]}
    >>> matchmaking(game_4=[], game_5=[45, 47, 48], game_6=[20, 26])
    {'game_4': 'not a fair game', 'game_5': 'not a fair game', \
'game_6': 'not a fair game'}
    >>> matchmaking(game_7=[250, 248, 253, 250, 251, 253],
    ... game_8=[250, 248, 253, 250, 251, 254])
    {'game_7': [253, 251, 253], 'game_8': 'not a fair game'}
    """
    output = {}
    for game_id in games:
        ranks = games[game_id]
        is_fair = is_fair_game(*ranks)

        if is_fair == False:
            output[game_id] = "not a fair game"
        else:
            average = sum(ranks) / len(ranks)
            output[game_id] = [x for x in ranks if x > average]

    return output


# Question 3
def count_even(nums):
    """
    Count the frequency of the multiples of 4 in the input `nums` list.
    You may assume the input list only contains non-negative integers.

    IMPORTANT: You should only use list comprehension for this question.

    >>> count_even([1, 10, 3, 8, 9, 7])
    1
    >>> count_even([1, 10, 3, 8, 9, 7, 13, 14, 2, 8])
    2
    >>> count_even([])
    0
    """
    return len([x for x in nums if (x % 4 == 0)])


# Question 4
def collect_args(*args, **kwargs):
    """
    Combine the positional arguments (*args) and keyword arguments (**kwargs)
    into a list of tuples. Each tuple contains the type of argument, position
    of this argument within `args` or `kwargs` (0-based indexing), and the
    value this argument holds. The specific format is shown below:

    Tuple for positional arguments:
    ("positional_1", 10), indicates the second positional argument is 10

    Tuple for keyword arguments:
    ("keyword_0_player1", [25, 30]), indicates the first keyword argument
    is called `player1` and holds the value `[25, 30]`

    IMPORTANT: You should only use list comprehension for this question.

    >>> collect_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> collect_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> collect_args(no_positional=True)
    [('keyword_0_no_positional', True)]
    """
    return [("positional_" + str(a), b) for a, b in enumerate(args)] + \
        [('keyword_{}_{}'.format(i, key), val) for i, (key, val) \
        in enumerate(kwargs.items())]


# Question 5
def count_hashtags(hashtags, posts):
    """
    Count the sum of how many times each specified hashtags appear in the
    posts and return the sum of these counts.

    IMPORTANT: You should only use list comprehension for this question.

    >>> count_hashtags([], [{'hashtags': ['quote'],
    ... 'text': 'Smart person solves bugs, and wise person avoids bugs'}])
    0
    >>> count_hashtags(['Elvy'],
    ... [{'hashtags': ['Elvy'], 'text': 'Elvy is the queen in piazza.'},
    ... {'hashtags': ['random'], 'text': 'this is such a random post.'}])
    1
    >>> count_hashtags(['DSC20', 'Debugging', 'Quiz'], \
[{'hashtags': ['school work', 'DSC20'], 'text': 'DSC20 is so much fun!'}, \
{'hashtags': ['Debugging', 'DSC20'], 'text': 'In order to debug, ' + \
'you have to be twice as smart as the person who writes the code!'}])
    3
    >>> count_hashtags(['Programming', 'Java'],
    ... [{'hashtags': ['Programming', 'Java'],
    ... 'text': 'javascript to java is carpet to car'},
    ... {'hashtags': [], 'text': 'javascript to java is carpet to car'}])
    2
    """
    return len([True for x in hashtags for y in posts if x in y['hashtags']])
