"""
DSC 20 Lab 08
Name: Willis Tan
PID:  A14522499
"""

# Question 1
def q1_doctests():
    """
    >>> player = Unit(200, 50, 10, (0,0))
    >>> cannon1 = Cannon(400, 25, 25, (50,0))
    >>> caster1 = Caster(100, 0, 30, (100,100))

    >>> player.attack(cannon1)
    'Attack successful'
    >>> cannon1.health
    350

    >>> player.attack(caster1)
    'Out of range'
    >>> caster1.health
    100
    >>> caster1.heal(50)
    >>> caster1.health
    150
    >>> caster1.move((35,35))
    >>> player.attack(caster1)
    'Attack successful'
    >>> caster1.health
    100

    >>> cannon1.attack(caster1)
    'Attack successful'
    >>> caster1.health
    50
    """
    return


class Unit:
    """
    A class that abstracts the character units of the game.
    """

    # TODO: define class attribute here
    attack_range = 50

    def __init__(self, health, attack_power, ability_power, location):
        """
        Constructor of Unit. Input validation not required

        Parameters:
            health (int): Health value of unit
            attack_power (int): Attack damage of unit
            ability_power (int): Ability power of unit
            location (tuple of ints (x, y)): Location of unit
        """
        # YOUR CODE GOES HERE #
        self.health = health
        self.attack_power = attack_power
        self.ability_power = ability_power
        self.location = location

    def calculate_dist(self, other_unit):
        """
        Calculates distance between self (Unit) and other_unit's locations
        Uses distance formula sqrt((x1-y1)^2 + (x2-y2)^2)
        """
        # YOUR CODE GOES HERE #
        x = (self.location[0] - other_unit.location[0])**2
        y = (self.location[1] - other_unit.location[1])**2
        return (x + y)**0.5

    def attack(self, other_unit):
        """
        Attacks other_unit for damage equal to Unit's attack_power
        (ability_power is not factored into damage in this case)

        Returns 'Attack successful' if attack is successful
            (other_unit in range)
        Returns 'Out of range' if attack cannot be performed (out of range)
        """
        # YOUR CODE GOES HERE #
        dist = self.calculate_dist(other_unit)
        if dist <= self.attack_range:
            other_unit.take_damage(self.attack_power)
            return 'Attack successful'
        else:
            return 'Out of range'

    def take_damage(self, val):
        """
        Reduce the health by `val`.
        """
        # YOUR CODE GOES HERE #
        self.health -= val

    def heal(self, val):
        """
        Increase the health by `val`.
        """
        # YOUR CODE GOES HERE #
        self.health += val

    def move(self, location):
        """
        Update the `location`.
        """
        # YOUR CODE GOES HERE #
        self.location = location


class Cannon(Unit):
    """
    A class that abstracts a cannon character.
    """

    # TODO: define class attribute here
    attack_range = 200

    def attack(self, other_unit):
        """
        Attack other_unit for damage equal to attack_power + ability_power

        Returns 'Attack successful' if attack is successful
            (other_unit in attack_range)
        Returns 'Out of range' if attack cannot be performed (out of range)
        """
        # YOUR CODE GOES HERE #
        dist = self.calculate_dist(other_unit)
        if dist <= self.attack_range:
            other_unit.take_damage(self.attack_power + self.ability_power)
            return 'Attack successful'
        else:
            return 'Out of range'


class Caster(Unit):
    """
    A class that abstracts a caster character.
    """

    # TODO: define class attribute here
    attack_range = 100

    def attack(self, other_unit):
        """
        Attack other_unit for damage equal to ability_power

        Returns 'Attack successful' if attack is successful
            (other_unit in attack_range)
        Returns 'Out of range' if attack cannot be performed (out of range)
        """
        # YOUR CODE GOES HERE #
        dist = self.calculate_dist(other_unit)
        if dist <= self.attack_range:
            other_unit.take_damage(self.ability_power)
            return 'Attack successful'
        else:
            return 'Out of range'


# Question 2
def q2_doctests():
    """
    >>> host = Host("Sean", -8)
    >>> p1 = Participant("Simon", 8)
    >>> p2 = Participant("Madeline", -8)
    >>> guest = Guest("James", -8)

    >>> host.send_to_all("Hey yall", 15)
    >>> host.outbox
    ['You send a message to Simon at 15: HEY YALL', \
'You send a message to Madeline at 15: HEY YALL', \
'You send a message to James(guest) at 15: HEY YALL']
    >>> host.inbox
    []
    >>> p1.inbox
    ['You receive a message from Sean(host) at 7: HEY YALL']
    >>> p2.inbox
    ['You receive a message from Sean(host) at 15: HEY YALL']
    >>> guest.inbox
    ['You receive a message from Sean(host) at 15: HEY YALL']

    >>> guest.send_to_all("Only to host", 11)
    >>> guest.outbox
    ['You send a message to Sean(host) at 11: Only to host']
    >>> host.inbox
    ['You receive a message from James(guest) at 11: Only to host']
    >>> p1.inbox
    ['You receive a message from Sean(host) at 7: HEY YALL']

    >>> guest.send_message(p1, "This message should not be sent", 6)
    >>> guest.outbox
    ['You send a message to Sean(host) at 11: Only to host']
    >>> p1.inbox
    ['You receive a message from Sean(host) at 7: HEY YALL']

    >>> p1.send_message(host, "This lab looks easy", 23)
    >>> p1.send_message(host, "I mean it is hard", 0)
    >>> p1.outbox
    ['You send a message to Sean(host) at 23: This lab looks easy', \
'You send a message to Sean(host) at 0: I mean it is hard']
    >>> host.inbox
    ['You receive a message from James(guest) at 11: Only to host', \
'You receive a message from Simon at 7: This lab looks easy', \
'You receive a message from Simon at 8: I mean it is hard']
    """
    return


class Participant:
    """
    A class that abstracts a participant in general.
    """

    # TODO: define class attribute here
    participant_list = []  # a list of all participants
    max_message_length = 50

    def __init__(self, display_name, time_zone):
        """
        Constructor of Participant. Input validation not required

        Parameters:
            display_name (str): Display name of Participant
            time_zone (int): Time zone of Participant, an offset from GMT
        """
        self.display_name = display_name
        self.time_zone = time_zone
        self.inbox = []
        self.outbox = []
        # We have implemented this class attribute for you!
        Participant.participant_list.append(self)

    def send_message(self, receiver, message, sender_time):
        """
        Sends message to receiver at sender_time
        1. Checks for message length, and terminates if it exceeds the limit
        2. Appends sender log to sender's outbox
        3. Appends receiver log to receiver's inbox
        """
        # YOUR CODE GOES HERE #
        if len(message) < self.max_message_length:
            receiver_time = (sender_time - (self.time_zone - receiver.time_zone)) % 24

            self.outbox.append("You send a message to {} at {}: {}".format(
                    receiver.display_name, sender_time, message
                )
            )
            receiver.inbox.append(
                "You receive a message from {} at {}: {}".format(
                    self.display_name, receiver_time, message
                )
            )
        else:
            return None


    def send_to_all(self, message, sender_time):
        """
        Sends message to all participants except the sender him/herself
        """
        # YOUR CODE GOES HERE #
        for p in self.participant_list:
            if not (p is self):
                self.send_message(p, message, sender_time)


class Host(Participant):
    """
    A class that abstracts a host.
    """

    # TODO: define class attribute here
    max_message_length = 50

    def __init__(self, display_name, time_zone):
        # YOUR CODE GOES HERE #
        # replace `pass` with your code; can be implemented in one line #
        super(Host, self).__init__(display_name + "(host)", time_zone)

    def send_message(self, receiver, message, sender_time):
        """
        A Host's message should be capitalized
        """
        # YOUR CODE GOES HERE #
        super(Host, self).send_message(receiver, message.upper(), sender_time)


class Guest(Participant):
    """
    A class that abstracts a guest.
    """

    # TODO: define class attribute here
    max_message_length = 15

    def __init__(self, display_name, time_zone):
        # YOUR CODE GOES HERE #
        # replace `pass` with your code; can be implemented in one line #
        super(Guest, self).__init__(display_name + "(guest)", time_zone)

    def send_to_all(self, message, sender_time):
        """
        A Guest who sends message with this method can only send to all Hosts
        """
        # YOUR CODE GOES HERE #
        for p in self.participant_list:
            if isinstance(p, Host):
                self.send_message(p, message, sender_time)
            