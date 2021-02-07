"""
DSC 20 Lab 10
Name: Willis Tan
PID:  A14522499
"""


# Question 1.1
class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """
        # YOUR CODE GOES HERE #
        self.items = []
        self.num_items = 0

    def size(self):
        """ Get the number of items stored. """
        # YOUR CODE GOES HERE #
        length = 0
        for i in self.items:
            length += 1
        return length

    def is_empty(self):
        """ Check whether the collection is empty. """
        # YOUR CODE GOES HERE #
        return self.size() == 0

    def clear(self):
        """ Remove all items in the collection. """
        # YOUR CODE GOES HERE #
        self.items = []


# Question 1.2
class Stack(Collection):
    """
    Stack class.

    >>> stk = Stack()
    >>> stk.size()
    0
    >>> stk.is_empty()
    True
    >>> str(stk)
    '(bottom) (top)'
    >>> stk.push(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> stk.push('LAB 10')
    >>> stk.size()
    1
    >>> stk.is_empty()
    False
    >>> stk.push('DSC')
    >>> stk.push(20)
    >>> stk.size()
    3
    >>> str(stk)
    '(bottom) LAB 10 -- DSC -- 20 (top)'
    >>> stk.pop()
    20
    >>> stk.pop()
    'DSC'
    >>> stk.peek()
    'LAB 10'
    >>> stk.size()
    1
    >>> stk.clear()
    >>> stk.pop()
    >>> stk.peek()
    """

    def push(self, item):
        """ Push `item` to the stack. """
        # YOUR CODE GOES HERE #
        if item is None:
            raise ValueError('item cannot be None')
        self.items.append(item)

    def pop(self):
        """ Pop the top item from the stack. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        return self.items.pop(-1)

    def peek(self):
        """ Peek the top item. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        return self.items[-1]

    def __str__(self):
        """ Return the string representation of the stack. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return "(bottom) (top)"
        return "(bottom) {} (top)".format(" -- ".join([str(x) for x in self.items]))


# Question 1.3
class Queue(Collection):
    """
    Queue class.

    >>> que = Queue()
    >>> que.size()
    0
    >>> que.is_empty()
    True
    >>> str(que)
    '(front) (rear)'
    >>> que.enqueue(None)
    Traceback (most recent call last):
    ...
    ValueError: item cannot be None
    >>> que.enqueue('LAB 10')
    >>> que.size()
    1
    >>> que.is_empty()
    False
    >>> que.enqueue('DSC')
    >>> que.enqueue(20)
    >>> que.size()
    3
    >>> str(que)
    '(front) LAB 10 -- DSC -- 20 (rear)'
    >>> que.dequeue()
    'LAB 10'
    >>> que.dequeue()
    'DSC'
    >>> que.peek()
    20
    >>> que.size()
    1
    >>> que.clear()
    >>> que.dequeue()
    >>> que.peek()
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        # YOUR CODE GOES HERE #
        if item is None:
            raise ValueError('item cannot be None')
        self.items.append(item)

    def dequeue(self):
        """ Dequeue the front item from the queue. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """ Peek the front item. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        return self.items[0]

    def __str__(self):
        """ Return the string representation of the queue. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return "(front) (rear)"
        return "(front) {} (rear)".format(" -- ".join([str(x) for x in self.items]))


# Question 2
def parentheses_checker(expression):
    """
    A function that checks whether all parentheses `{}, [], ()`
    are balanced in the given `expression`.

    >>> parentheses_checker("(((]})")
    False
    >>> parentheses_checker("(")
    False
    >>> parentheses_checker("(){}[]]")
    False
    >>> parentheses_checker("(   x   )")
    True
    >>> parentheses_checker("a()b{}c[]d")
    True
    >>> parentheses_checker("")
    True
    """
    # YOUR CODE GOES HERE #
    left_paran = Stack()
    for char in expression:
        if char in set(['{', '(', '[']):
            left_paran.push(char)
        elif char in set(['}', ')', ']']):
            if (left_paran.is_empty()):
                return False

            top_of_stack = left_paran.peek()
            if (top_of_stack == '{' and char == '}') \
                or (top_of_stack == '[' and char == ']') \
                or (top_of_stack == '(' and char == ')'):
                left_paran.pop()
    return left_paran.is_empty()


# Question 3
def inf_skip_increasing(iterable):
    """
    A generator that takes in an `iterable` object and infinitely yields its
    items. This generator skips items by an increasing amount after each
    yield. If this generator reached the end of the `iterable`, proceed from
    the front.

    >>> gen = inf_skip_increasing(range(10))
    >>> next(gen)
    0
    >>> next(gen)
    1
    >>> [next(gen) for _ in range(10)]
    [3, 6, 0, 5, 1, 8, 6, 5, 5, 6]
    """
    # YOUR CODE GOES HERE #
    def generator():
        queue = Queue()
        for item in iterable:
            queue.enqueue(item)
        n_skips = 0
        while True:
            yield queue.peek()
            # move the yielded item to the back
            item = queue.dequeue()
            queue.enqueue(item)

            # move the next n_skip items to the back
            for i in range(n_skips):
                item = queue.dequeue()
                queue.enqueue(item)
            # increment n_skips by 1 for the next iteration
            n_skips += 1

    return generator()
