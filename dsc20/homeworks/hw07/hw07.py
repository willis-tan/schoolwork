"""
DSC 20 Homework 07
Name: Willis Tan
PID:  A14522499
"""

def doctests_go_here():
    """
    >>> available_time1 = [[1, 3, 21], [4, 6, 30], [9, 12, 8]]
    >>> ps1 = PersonalSchedule("Sun", "Curly", available_time1)
    >>> print(ps1)
    Curly Sun is available at [[1, 3, 21], [4, 6, 30], [9, 12, 8]].

    >>> available_time2 = [[1, 7, 20], [9, 10, 5], [11, 16, 8]]
    >>> ps2 = PersonalSchedule("Ran", "Sean", available_time2)
    >>> print(ps2)
    Sean Ran is available at [[1, 7, 20], [9, 10, 5], [11, 16, 8]].

    >>> t1 = Task(2, 5, 20, 1000, "Chopping potatoes")
    >>> t2 = Task(4, 5, 32, 2000, "Coding")
    >>> t3 = Task(11, 12, 8, 4000, "Playing League")
    >>> t4 = Task(1, 2, 21, 1200, "Gardening")
    >>> t5 = Task(11, 16, 6, 500, "Jogging")
    >>> t6 = Task(4, 6, 20, 1200, "Chopping potatoes")
    >>> t7 = Task(6, 9, 20, 1000, "Chopping potatoes")

    >>> print(t1)
    Task Chopping potatoes starts at 2, ends at 5, requires 20 focus level, \
and gives 1000 profit.

    >>> print(t2)
    Task Coding starts at 4, ends at 5, requires 32 focus level, and gives \
2000 profit.

    >>> print(t3)
    Task Playing League starts at 11, ends at 12, requires 8 focus level, \
and gives 4000 profit.

    >>> ps1.can_handle(t1)
    False
    >>> ps1.can_handle(t2)
    False
    >>> ps1.can_handle(t3)
    True
    >>> ps2.can_handle(t4)
    False
    >>> ps2.can_handle(t5)
    True

    >>> ps1.can_handle_task_sequence([t1, t2, t3])
    False
    >>> ps1.can_handle_task_sequence([t3, t4])
    True
    >>> ps2.can_handle_task_sequence([t3, t4])
    False
    >>> ps2.can_handle_task_sequence([t3, t5])
    True

    >>> t1.can_merge_task(t6)
    True
    >>> t1.can_merge_task(t7)
    False

    >>> merged_task1 = t1.merge_two_tasks(t6)
    >>> print(merged_task1)
    Task Chopping potatoes starts at 2, ends at 6, requires 20 focus level, \
and gives 2200 profit.
    >>> merged_task2 = t1.merge_two_tasks(t7)
    >>> print(merged_task2)
    None

    >>> task_sequences = [[t1, t2, t3], [t3, t4], [t3, t6]]
    >>> result1 = ps1.most_profitable_task_sequence(task_sequences)
    >>> result2 = ps1.most_profitable_task_sequence_recursion(task_sequences)
    >>> result1 == [[t3, t4], [t3, t6]]
    True
    >>> result1 == result2
    True

    >>> result3 = ps2.most_profitable_task_sequence_recursion([[t3], [t5]])
    >>> result3 == [[t3]]
    True

    >>> ps2.handle_two_tasks(t1, t6)
    True
    >>> ps2.handle_two_tasks(t1, t7)
    False
    >>> ps2.handle_two_tasks(t6, t7)
    False
    """
    return


class Task:
    """
    Implementation of a task.
    """

    def __init__(self, start_time, end_time, focus_level_required, \
                profit, task_description):
        """
        Constructor of Task.

        Requirement:
        Input validation

        Parameters:
        start_time (int): Start time of this task should be a non-negative integer.
        end_time (int): End time of this task should also be a non-nagative integer.
                        Start time should be strictly less than end time.
        focus_level_required (int): Focus level required for one person to handle
                        this task. It should be a positive integer.
        profit (int): A positive integer that represents how much value would
                        be made if the task is successfully handled.
        task_description (str): Description of this task.
        """
        # YOUR CODE STARTS HERE #
        ints = [start_time, end_time, focus_level_required, profit]
        assert all(isinstance(x, int) for x in ints)
        assert start_time >= 0 and end_time >= 0
        assert end_time >= start_time
        assert profit >= 1
        assert isinstance(task_description, str)

        self.start_time = start_time
        self.end_time = end_time
        self.focus_level_required = focus_level_required
        self.profit = profit
        self.task_description = task_description


    def get_start_time(self):
        """Getter for start_time attribute"""
        # YOUR CODE STARTS HERE #
        return self.start_time


    def get_end_time(self):
        """Getter for end_time attribute"""
        # YOUR CODE STARTS HERE #
        return self.end_time


    def get_focus_level_required(self):
        """Getter for focus_level_required attribute"""
        # YOUR CODE STARTS HERE #
        return self.focus_level_required


    def __str__(self):
        """
        String representation of Task.
        """
        return ("Task {} starts at {}, ends at {}, requires {} focus level, " + \
                "and gives {} profit.").format(self.task_description, \
                self.get_start_time(), self.get_end_time(), \
                self.get_focus_level_required(), self.profit)


    def can_merge_task(self, other_task):
        """
        Give another Task called other_task, this function determines whether
        we are able to merge the current task and other_task.

        Requirement:
        Input validation

        Parameters
        other_task (Task): The other task to be merged with this task.

        Returns:
        True if we are able to merge those two tasks, False otherwise.
        """
        # YOUR CODE STARTS HERE #
        self_start = self.get_start_time()
        other_start = other_task.get_start_time()
        self_end = self.get_end_time()
        other_end = other_task.get_end_time()
        overlap = range(
            max(self_start, other_start), 
            min(self_end, other_end) + 1
        )

        return (
            self.get_focus_level_required() \
            == other_task.get_focus_level_required()
            ) \
            and \
            len(overlap) > 0 \
            and \
            self.task_description == other_task.task_description
            


    def merge_two_tasks(self, other_task):
        """
        Merge two tasks if the merge is possible.

        Requirement:
        Input validation

        Parameters:
        other_task (Task): The other task to be merged with this task.

        Returns:
        The Task object after merging two tasks, where the new profit is the sum
        of two tasks' profit; otherwise, None is returned.
        """
        # YOUR CODE STARTS HERE #
        if self.can_merge_task(other_task):
            new_start = min(self.get_start_time(), other_task.get_start_time())
            new_end = max(self.get_end_time(), other_task.get_end_time())
            new_profit = self.profit + other_task.profit
            return Task(
                new_start, 
                new_end, 
                self.get_focus_level_required(), 
                new_profit,
                self.task_description
            )
        else:
            return None


class PersonalSchedule:
    """
    Implementation of a personal schedule.
    """

    def __init__(self, last_name, first_name, available_time):
        """
        Constructor of PersonalSchedule.

        Requirement:
        Input validation

        Parameters:
        last_name (str): Last name of this person. This string must have at least 2
                        characters.
        first_name (str): First name of this person. This string must have at least 2
                        characters.
        available_time (list[list]): A list of available intervals. Each interval has
                        three elements: [start_time, end_time, focus_level]. You
                        may assume that given intervals don't have overlaps with
                        one another.
        """
        # YOUR CODE STARTS HERE #
        MIN_NAME_LENGTH = 2

        assert len(last_name) > MIN_NAME_LENGTH and \
            len(first_name) > MIN_NAME_LENGTH
        assert isinstance(last_name, str) and isinstance(first_name, str)
        assert isinstance(available_time, list)

        for inner_lst in available_time:
            assert isinstance(inner_lst, list)
            for elem in inner_lst:
                assert isinstance(elem, int)

        self.last_name = last_name
        self.first_name = first_name
        self.available_time = available_time


    def get_last_name(self):
        """Getter for last_name attribute"""
        # YOUR CODE STARTS HERE #
        return self.last_name


    def get_first_name(self):
        """Getter for first_name attribute"""
        # YOUR CODE STARTS HERE #
        return self.first_name


    def get_available_time(self):
        """Getter for available_time attribute"""
        # YOUR CODE STARTS HERE #
        return self.available_time


    def __str__(self):
        """
        String representation of PersonalSchedule.
        """
        return "{} {} is available at {}.".format(self.get_first_name(), \
                self.get_last_name(), self.get_available_time())


    def can_handle(self, task):
        """
        This function determines whether this person can handle the given task.

        Requirement:
        Input validation

        Parameters:
        task (Task): A task that this person needs to handle.

        Returns:
        True if there exists a time interval in the schedule that can properly
        handle the task with the required focus level, False otherwise.
        """
        # YOUR CODE STARTS HERE #
        FOCUS_LVL_IDX = 2
        task_start = task.get_start_time()
        task_end = task.get_end_time()
        for interval in self.get_available_time():
            if interval[FOCUS_LVL_IDX] >= task.get_focus_level_required() and\
                (interval[0] <= task_start <= task_end <= interval[1]):
                return True
        
        return False


    def can_handle_task_sequence(self, task_sequence):
        """
        Given a list of tasks, this function determines whether this person
        can handle this task sequence.

        Requirement:
        Input validation

        Parameters:
        task_sequence (list[Task]): A list of tasks this person needs to handle.

        Returns:
        True if all tasks can be properly handled, False otherwise. To simplify
        the question, we assume that multitasking is possible, i.e., a person
        can handle multiple tasks in a single time interval.
        """
        # YOUR CODE STARTS HERE #
        for task in task_sequence:
            if not self.can_handle(task):
                return False
        return True


    def most_profitable_task_sequence(self, task_sequences):
        """
        Given a list of task sequences, find all task sequences that give you
        the maximum profit.

        Requirement:
        Input validation

        Parameters:
        task_sequences (list[list]): A list of task sequences.

        Return:
        Sequence(s) of tasks (that a person can handle)  that gives you the most profit. 
        """
        # YOUR CODE STARTS HERE #
        profits = []
        for t_seq in task_sequences:
            if self.can_handle_task_sequence(t_seq):
                profits.append(sum([t.profit for t in t_seq]))
            else:
                profits.append(0)
        
        if all(map(lambda p: p == 0, profits)):
            return task_sequences
        else:
            valid_seq = list(zip(task_sequences, profits))
            max_profit = max(profits)
            return [elem[0] for elem in valid_seq if elem[1] == max_profit]
            


    def most_profitable_task_sequence_recursion(self, task_sequences):
        """
        Given a list of task sequences, find all task sequences that give you
        the maximum profit.
        You MUST USE RECURSION in your solution.

        Requirement:
        Input validation

        Parameters:
        task_sequences (list[list]): A list of task sequences.

        Return:
        Sequence(s) of tasks (that a person can handle)  that gives you the most profit. 

        """
        # YOUR CODE STARTS HERE #
        if len(task_sequences) == 1: 
            return task_sequences 
        else:
            
            return 0


    def handle_two_tasks(self, task1, task2):
        """
        Given two tasks, the function determines whether this personal can handle
        them together.

        Requirement:
        Input validation

        Parameters:
        task1 (Task): The first task.
        task2 (Task): The second task.

        Returns:
        True if and only if two tasks can be merged and handled by this PersonalSchedule,
        False otherwise.
        """
        # YOUR CODE STARTS HERE #
        merged = task1.merge_two_tasks(task2)
        if merged != None and self.can_handle(merged):
            return True
        else:
            return False

# END OF FILE #
