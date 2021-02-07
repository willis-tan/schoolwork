"""
DSC 20 Lab 07
Name: Willis Tan
PID:  A14522499
"""

# Question 1
def reverse_half(lst):
    """
    Given input list lst, reverse the last half of the list,
    starting from the middle (len//2). You must do this in-place.
    You may not use lst[::-1] or similar techniques.
    Do not return anything.

    >>> lst1 = [0, 1, 2, 3, 4, 5, 6]
    >>> reverse_half(lst1)
    >>> lst1
    [0, 1, 2, 6, 5, 4, 3]

    >>> lst2 = []
    >>> reverse_half(lst2)
    >>> lst2
    []

    >>> lst3 = [0, 1, 2, 3, 4, 5, 6, 7]
    >>> reverse_half(lst3)
    >>> lst3
    [0, 1, 2, 3, 7, 6, 5, 4]
    """
    middle = len(lst) // 2

    i = len(lst) - 1
    while middle < i:
        lst[middle], lst[i] = lst[i], lst[middle]
        middle += 1
        i -= 1


# Question 2
def split_even_odd(lst1, lst2, even=True):
    """
    Given two lists of equal length lst1 and lst2,
    if even is True, swap all of the values at the even indices.
    If even is False, swap all of the values at the odd indices.
    Do not return anything.

    >>> lst1 = [0, 1, 2, 3, 4]
    >>> lst2 = [5, 6, 7, 8, 9]
    >>> split_even_odd(lst1, lst2, True)
    >>> lst1
    [5, 1, 7, 3, 9]
    >>> lst2
    [0, 6, 2, 8, 4]

    >>> split_even_odd(lst1, lst2, False)
    >>> lst1
    [5, 6, 7, 8, 9]
    >>> lst2
    [0, 1, 2, 3, 4]

    >>> empty1 = []
    >>> empty2 = []
    >>> split_even_odd(empty1, empty2)
    >>> empty1
    []
    >>> empty2
    []
    """
    # YOUR CODE GOES HERE #
    if even:
        for i in range(0, len(lst1), 2):
            lst1[i], lst2[i] = lst2[i], lst1[i]
    else:
        for i in range(1, len(lst1), 2):
            lst1[i], lst2[i] = lst2[i], lst1[i]


# Question 3
def separate_dicts(dict1, dict2):
    """
    Given two dictionaries dict1 and dict2,
    mutate the dictionaries such that all keys with odd length
    are kept/moved into dict1 and all keys with even length
    are kept/moved into dict2.
    If there are items with the same key, add their values together.
    Do not return anything. You cannot use another dictionary.

    >>> dict1 = {'a': 10, 'b': 5, 'ab': 7}
    >>> dict2 = {'ab': 20, 'b': 1, 'z': 0, 'hihi': 1}
    >>> separate_dicts(dict1, dict2)
    >>> sorted(dict1)
    ['a', 'b', 'z']
    >>> [dict1[i] for i in sorted(dict1)]
    [10, 6, 0]
    >>> sorted(dict2)
    ['ab', 'hihi']
    >>> [dict2[i] for i in sorted(dict2)]
    [27, 1]
    """
    # YOUR CODE GOES HERE #
    key1 = list(dict1.keys())
    key2 = list(dict2.keys())
    for key in key1:
        if len(key) % 2 == 0:
            if key in key2:
                dict2[key] += dict1[key]
            else: dict2[key] = dict1[key]
            del dict1[key] 

    for key in key2:
        if len(key) % 2 == 1:
            if key in key1:
                dict1[key] += dict2[key]
            else: dict1[key] = dict2[key]
            del dict2[key]


# Question 4
class Dishwasher:
    """
    Creates a class with 1 class attribute and two class methods

    >>> Dishwasher.brand
    'Boah'
    >>> Dishwasher.start()
    'Spins and Cleans'
    >>> Dishwasher.broke()
    'Stops and Leaks'
    """
    brand = 'Boah'
    
    def start():
        return 'Spins and Cleans'
    def broke():
        return 'Stops and Leaks'


# Question 5
class Stove:
    """
    >>> stove = Stove("GM", "pie", 350)
    >>> stove.brand
    'GM'
    >>> stove.dish
    'pie'
    >>> stove.temp
    350
    >>> stove.change_temp(400)
    >>> stove.change_dish('beans')
    >>> stove.what_is_cooking_what_temp()
    'beans at 400'
    >>> stove.change_temp(450)
    >>> stove.what_is_cooking_what_temp()
    'beans at 450'
    """
    def __init__(self, brand, dish, temp):
        self.brand = brand
        self.dish = dish
        self.temp = temp

    def change_temp(self, new_temp):
        self.temp = new_temp

    def change_dish(self, new_dish):
        self.dish = new_dish

    def what_is_cooking_what_temp(self):
        return self.dish + " at " + str(self.temp)

# Question 6
class Phone:
    """
    Creates a Phone class with 5 class attributes (charge, drain_rate,
    charge_rate, num_apps, apps), 3 instance attributes (brand, battery,
    storage), and 3 methods (use, recharge, install)

    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Robinhood')
    'App installed'
    >>> my_phone.apps
    {'Robinhood'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    """
    # Initializer
    def __init__(self, brand, battery, storage):
        self.brand = brand
        self.battery = battery
        self.storage = storage
        self.charge = battery // 2
        # Drain rate will differ based on brand
        # Create if-else structure
        if self.brand == 'Apple':
            self.drain_rate = 10
        elif self.brand == 'OnePlus':
            self.drain_rate = 12
        elif self.brand == 'Samsung':
            self.drain_rate = 8
        else:
            self.drain_rate = 15

        self.charge_rate = 20
        self.num_apps = 0
        self.apps = set()

    def use(self, minutes):
        # TODO: Update charge
        spent = minutes * self.drain_rate
        
        if self.charge > spent:
            self.charge -= spent
        else:
            self.charge = 0
            return 'Out of charge'

    def recharge(self, minutes):
        # TODO: Update charge
        self.charge = self.charge + minutes * self.charge_rate
        if self.charge > self.battery:
            self.charge = self.battery

    def install(self, app_size, app_name):
        # Cannot install apps when we don't have charge
        if self.charge == 0:
            return 'Out of charge'
        # Cannot install apps when we don't have sufficient storage
        if self.storage < app_size:
            return 'Not enough storage'
        # Cannot install apps that are already installed
        if app_name in self.apps:
            return 'App already installed'

        # Have dealt with all potential issues. Install app now
        # TODO: Update storage
        self.storage -= app_size
        # TODO: Update num_apps
        self.num_apps += 1
        # TODO: Update apps
        self.apps.add(app_name)
        return 'App installed'
