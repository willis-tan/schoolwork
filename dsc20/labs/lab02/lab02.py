"""
DSC 20 Lab 02
Name: Willis Tan
PID:  A14522499
"""

# Question 1
def check_Blackjack(player1, player2):
    """
    Returns a list of results of the Blackjack game between player1 and
    player 2. For the i-th round, the i-th index of player1 list represents
    the sum of all cards of player1, and the i-th index of player2 list
    represents player2's card sum. The i-th index of the returned list should
    be the winner's card sum. If the card sum is closer to 21 but not going
    over it, that player wins. If both players' card sum go over 21 in a
    round, we put 0 for that round instead.

    Parameters:
        player1 (List[int]): card sums for player 1
        player2 (List[int]): card sums for player 2

    Returns:
        (List[int]): game results judged with the rule above

    Assumptions:
        player1 and player2 will always have the same length

    >>> check_Blackjack([19, 21, 22], [21, 19, 3])
    [21, 21, 3]
    >>> check_Blackjack([17, 21, 22, 29], [15, 19, 3, 4])
    [17, 21, 3, 4]
    >>> check_Blackjack([], [])
    []
    """
    
    blackjacks = []
    num_rounds = len(player1)

    for i in range(num_rounds):
        sum1 = player1[i]
        sum2 = player2[i]

        if sum1 > 21:
            sum1 = 0
        if sum2 > 21:
            sum2 = 0

        if (sum1 >= sum2):
            blackjacks.append(sum1)
        elif (sum1 <= sum2):
            blackjacks.append(sum2)

    return blackjacks


# Question 2
def majority_element(nums):
    """
    Returns the majority element in the `nums` list. The majority element
    is the element that appears more than ⌊ n/2 ⌋ times, where n is the length
    of `nums` list.

    Parameters:
        nums (List[int]): the list of integers to apply this function

    Returns:
        (int) the majority element found

    Assumptions:
        `nums` list is non-empty
        A majority element always exists in `nums` list

    >>> majority_element([3,2,3])
    3
    >>> majority_element([2,2,1,1,1,2,2])
    2
    >>> majority_element([1,1,2,2,2])
    2
    """
    # YOUR CODE GOES HERE #    
    counts = dict((x, nums.count(x)) for x in set(nums))
    return max(counts, key = counts.get)

# Question 3
def remove_vowels(string):
    """
    Removes vowels (a, e, i, o, u) from `string` and returns the resulted
    string. Capitalized vowel letters should also be removed.

    Parameters:
        string (str): the string to apply this function

    Returns:
        (str): the string with vowel letters removed

    >>> remove_vowels('Hello')
    'Hll'
    >>> remove_vowels('')
    ''
    >>> remove_vowels('Hi how are...you?')
    'H hw r...y?'
    """
    # YOUR CODE GOES HERE #
    vowels = {
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    }

    output = ''
    for char in string:
        if char not in vowels:
            output = output + char

    return output


# Question 4
def pig_latin(string):
    """
    Returns `string` translated into Pig Latin. Please read the write-up
    for specific rules of translating a string into Pig Latin.

    However, for whatever reason we are afraid of 8 letter words. If we
    encounter a 8 letter word, we will immediately stop translating and
    return what we have translated so far.

    Parameters:
        string (str): the string to translate

    Returns:
        (str): the translated string

    Assumptions:
        there will be no punctuation in `string`.
        all words will only be separated by one space.
        all words will have at least one vowel.

    >>> pig_latin('Hi how are you')
    'iHay owhay areyay ouyay'
    >>> pig_latin('Absolute')
    ''
    >>> pig_latin('When words begin with consonant clusters')
    'enWhay ordsway eginbay ithway onsonantcay'
    """
    # YOUR CODE GOES HERE #
    words = string.split()
    vowels = {
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    }
    translated = []
    for word in words:
        if len(word) == 8:
            break
        else:
            if word[0] in vowels:
                translated.append(word + "yay")
            else:
                index = 0
                for char in word:
                    if char not in vowels:
                        index += 1
                    else:
                        break

                translated.append(word[index:] + word[: index] + "ay")
    return " ".join(translated)
