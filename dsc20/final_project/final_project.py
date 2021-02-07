"""
DSC 20 Final Project
Name: Willis Tan
PID:  A14522499
"""
from util import Stack, Queue
from datetime import datetime


def doctest():
    """
    ------------------------ PRODUCT TEST ------------------------

    >>> p1 = Product("iphone",399)
    >>> p2 = Special_Product("macbook air",999)
    >>> p3 = Limited_Product("free iphone", 0, 10)
    >>> p1, p2, p3
    (PRODUCT <0>, PRODUCT <1>, PRODUCT <2>)
    >>> print(p1)
    <0> iphone - 399$
    >>> print(p2)
    <1> macbook air - 999$ (special)
    >>> print(p3)
    <2> free iphone - 0$ (10 left)

    ------------------------ WAREHOUSE TEST ------------------------

    >>> wh = Warehouse()
    >>> st = Store(wh)
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> print(wh)
    Warehouse with 3 products
    >>> print(wh.get_product(1))
    <1> macbook air - 999$ (special)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <0> iphone - 399$
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (10 left)
    ============================
    >>> wh.export_product(3)
    >>> wh.export_product(2)
    PRODUCT <2>
    >>> wh.remove_product(0)
    True
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (9 left)
    ============================
    >>> st.view_products(sort = True)
    ============================
    <ID> Product - Price
    <2> free iphone - 0$ (9 left)
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.remove_product(0)
    False
    >>> [wh.export_product(2) for i in range(9)]
    [PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>,\
 PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>]
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.show_log()
    Product <0> imported - 2020-11-26 07:09:17.709522
    Product <1> imported - 2020-11-26 07:09:17.709584
    Product <2> imported - 2020-11-26 07:09:17.709612
    Product <2> exported - 2020-11-26 07:09:17.709745
    Product <0> removed  - 2020-11-26 07:09:17.709776
    Product <2> exported - 2020-11-26 07:09:17.709886
    Product <2> exported - 2020-11-26 07:09:17.709893
    Product <2> exported - 2020-11-26 07:09:17.709897
    Product <2> exported - 2020-11-26 07:09:17.709901
    Product <2> exported - 2020-11-26 07:09:17.709905
    Product <2> exported - 2020-11-26 07:09:17.709909
    Product <2> exported - 2020-11-26 07:09:17.709913
    Product <2> exported - 2020-11-26 07:09:17.709916
    Product <2> exported - 2020-11-26 07:09:17.709920
    Product <2> removed  - 2020-11-26 07:09:17.709924

    ------------------------ USER TEST ------------------------

    >>> u1 = User( 'Jerry', st)
    >>> u2 = Premium_User( 'FYX', st)
    >>> u1
    USER<0>
    >>> u2
    USER<1>
    >>> print(u1)
    standard user: Jerry - 0$
    >>> u2.add_balance(2000)
    >>> print(u2)
    premium user: FYX - 2000$
    
    >>> wh.import_product(p1)
    >>> u1 = User("A",st)
    >>> u1.add_cart(0)
    >>> u1.add_cart(0)
    >>> u1.view_cart()
    (front) <0> iphone - 399$ -- <0> iphone - 399$ (rear)
    >>> u1.checkout()
    STORE: Not enough money QQ
    []
    >>> u1.add_balance(1000)
    >>> u1.checkout()
    STORE: A ordered iphone. A has 562$ left.
    STORE: A ordered iphone. A has 124$ left.
    [PRODUCT <0>, PRODUCT <0>]
    >>> p4 = Limited_Product("Ipad", 600, 5)
    >>> wh.import_product(p4)
    >>> u2.buy_all(3)
    STORE: FYX ordered Ipad. FYX has 1400$ left.
    STORE: FYX ordered Ipad. FYX has 800$ left.
    STORE: FYX ordered Ipad. FYX has 200$ left.
    STORE: Not enough money QQ
    [PRODUCT <3>, PRODUCT <3>, PRODUCT <3>]

    ------------------- HISTORY / UNDO TEST -------------------

    >>> u1.view_history()
    (bottom) <0> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903632 -- \
<1> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903658 (top)
    >>> u1.undo_purchase()
    STORE: A refunded iphone. A has 523$ left.

    -------------------------- EC TEST ------------------------
    >>> p1 = Product("A",20)
    >>> p2 = Special_Product("B",7)
    >>> p3 = Limited_Product("C", 1, 2)
    >>> wh = Warehouse()
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> st = Store(wh)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <4> A - 20$
    <5> B - 7$ (special)
    <6> C - 1$ (2 left)
    ============================
    >>> st.so_rich(45)
    1
    >>> st.so_rich(61)
    0
    >>> st.so_rich_recursive(45)
    1
    >>> st.so_rich_recursive(61)
    0
    """
    pass


#######################################################################
#                               PRODUCT                               #
#######################################################################
class Product:
    """
    The Product class serves as an abstraction for products available to
    stores. 
    """

    product_counter = 0

    ##### Part 1.1 #####
    def __init__(self, name, price):
        """
        Constructor for Product instances. Each Product instance is initialized
        with a product's name and price.
        Each instance has instance attributes name, price, and id. The id
        starts at 0 and increments by 1 each time a new Product Instance is
        initialized.
        """
        # YOUR CODE GOES HERE #
        self.name = name
        self.price = price
        self.id = Product.product_counter
        Product.product_counter += 1

    def __str__(self):
        """
        Returns the string representation as: "<{id}> {name} - {price}$"
        """
        # YOUR CODE GOES HERE #
        return '<{}> {} - {}$'.format(self.id, self.name, self.price)

    def __repr__(self):
        """
        Returns the string representation as: "PRODUCT <{id}>"
        """
        # YOUR CODE GOES HERE #
        return 'PRODUCT <{}>'.format(self.id)


class Limited_Product(Product):
    """
    The Limited_Product class is a child class of the Product class.
    Limited products are products that have limited amounts.
    """

    ##### Part 1.2 #####
    def __init__(self, name, price, amount):
        """
        Constructor for Limited_Product instances. Each Limited_Product is
        initialized with name, price, and amount. They share the same instance
        attributes as Product, including id. Limited_Product has an extra
        attribute, amount.
        """
        # YOUR CODE GOES HERE #
        super().__init__(name, price)
        self.amount = amount

    def __str__(self):
        """
        Returns the string representation as: 
        "<{id}> {name} - {price}$ ({amount} left)"
        """
        # YOUR CODE GOES HERE #
        return '<{}> {} - {}$ ({} left)'.format(
            self.id, 
            self.name, 
            self.price, 
            self.amount
        )


class Special_Product(Product):
    """
    Special_Product class is a child class of the Product class. Special
    products are only to be purchased by premium users.
    """

    ##### Part 1.3 #####
    def __init__(self, name, price, description="special"):
        """
        Constructor for Special_Product instances. Each instance is initialized
        with name, price, and a description. If no description is provided, the
        default description is "special". Special_Product share the same
        attributes as Product, but has an extra attribute, description.
        """
        # YOUR CODE GOES HERE #
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        """
        Returns the string representation as: 
        "<{id}> {name} - {price}$ ({description})"
        """
        # YOUR CODE GOES HERE #
        return "<{}> {} - {}$ ({})".format(
            self.id, 
            self.name, 
            self.price, 
            self.description
        )


#######################################################################
#                              WAREHOUSE                              #
#######################################################################


class Warehouse:
    """
    Warehouse class serves as an abstraction for a warehouse that stores all
    the products that a store sells.
    """

    ##### Part 2 #####
    def __init__(self):
        """
        Constructor for Warehouse instances. Each instance has instance
        attributes, inventory and log. Inventory is a dictionary that stores
        all products as product id, product instance key-value pairs. Log is a
        list that stores all the import, export, removals records.
        """
        # YOUR CODE GOES HERE #
        self.inventory = dict()
        self.log = []

    def __str__(self):
        """
        Returns the string representation as: 
        "Warehouse with {number of products stored} products"
        """
        # YOUR CODE GOES HERE #
        return "Warehouse with {} products".format(len(self.inventory))

    def get_product(self, product_id):
        """
        Returns the product with the given id.
        If the product is not in the warehouse, return None.
        """
        # YOUR CODE GOES HERE #
        return self.inventory.get(product_id)

    def list_products(self):
        """
        Returns a list of product instances stored in the warehouse
        """
        # YOUR CODE GOES HERE #
        return list(self.inventory.values())

    def remove_product(self, product_id):
        """
        Removes the product instance with the given id from the warehouse.
        Return true if successfully removed, else false.
        If successfully removed a message will added to the log as so:
        "Product <{product id}> removed  - {time}"
        """
        # YOUR CODE GOES HERE #
        removed = self.inventory.pop(product_id, None)
        if removed != None:
            self.log.append("Product <{}> removed  - {}".format(
                    product_id, 
                    datetime.now()
                )
            )
            return True
        else:
            return False

    def import_product(self, product):
        """
        Import the product instance into the inventory. If the product is
        already in inventory, nothing is done.

        After importing, add a message to the log as so:
        "Product <{product id}> imported - {time}"
        """
        # YOUR CODE GOES HERE #
        if product.id in self.inventory:
            pass
        else:
            self.inventory[product.id] = product
            self.log.append("Product <{}> imported - {}".format(
                    product.id, 
                    datetime.now()
                )
            )

    def export_product(self, product_id):
        """
        Export the product with the given id from inventory. If the product is
        not in inventory, do nothing.
        Return the instance of the exported product. If the product is a
        limited product, then also decrement the amount of that product in
        inventory by 1 each time it is exported. If the amount left reaches 0,
        remove the product from inventory.

        After exporting, add a message to the log as so:
        "Product <{product id}> exported - {time}"
        """
        # YOUR CODE GOES HERE #
        item = self.get_product(product_id)
        if item == None:
            return None
        else:
            self.log.append("Product <{}> exported - {}".format(
                    product_id, 
                    datetime.now()
                )
            )
            if isinstance(item, Limited_Product):
                item.amount -= 1
                if item.amount == 0:
                    self.remove_product(product_id)
            return item

    def size(self):
        """
        Return the number of distinct products stored in inventory
        """
        # YOUR CODE GOES HERE #
        return len(self.inventory)

    def show_log(self):
        """
        For each message in the log book, print them all on seperate lines.
        """
        # YOUR CODE GOES HERE #
        for msg in self.log:
            print(msg)


#######################################################################
#                               HISTORY                               #
#######################################################################
class History:
    """
    History class is an abstraction for purchase histories. After successful
    orders, a History instance is generated for users to add to their purchase
    history.
    """

    ##### Part 3 #####
    history_counter = 0
    def __init__(self, product, user):
        """
        Constructor for History instances. Each instance is initialized with
        a Product instance and a User instance. Instance attributes are
        product, user, an ID that behaves the same as the product ID, and the
        time when this instance was created.
        """
        self.product = product
        self.user = user
        self.id = History.history_counter
        History.history_counter += 1
        self.time = datetime.now()

    def __str__(self):
        """
        Return the string representation as:
        "<{history id}> {user id} bought {product} at {time}"
        """
        # YOUR CODE GOES HERE #
        return "<{}> {} bought {} at {}".format(
            self.id, 
            self.user.id, 
            self.product, 
            datetime.now()
        )

    def __repr__(self):
        """
        Return the string representation as:
        "HISTORY<{history id}> - {time}"
        """
        # YOUR CODE GOES HERE #
        return "HISTORY<{}> - {}".format(self.id, datetime.now())


#######################################################################
#                                USER                                 #
#######################################################################
class User:
    """
    User class serves as an abstraction for users. Users are only allowed to
    shop at only one store. User instances are treated as regular users.
    """
    ##### Part 4.1 #####
    user_counter = 0
    def __init__(self, name, store):
        """
        Constructor for User instances. Each instance is initialized with the
        user's username and the store they shop at. Instance attributes are:
        name, store, balance, their user ID, purchase history, and shopping
        cart.
        """
        # YOUR CODE GOES HERE #
        self.name = name
        self.store = store
        self.balance = 0
        self.id = User.user_counter
        User.user_counter += 1
        self.purchase_history = Stack()
        self.cart = Queue()
        self.store.add_user(self)

    def __str__(self):
        """
        Return the string representation as:
        "standard user: {name} - {balance}$"
        """
        # YOUR CODE GOES HERE #
        return "standard user: {} - {}$".format(self.name, self.balance)

    def __repr__(self):
        """
        Return the string representation as:
        "USER<{id}>"
        """
        # YOUR CODE GOES HERE #
        return "USER<{}>".format(self.id)

    def set_name(self, new_name):
        """
        Replaces a user's old name to new_name
        """
        # YOUR CODE GOES HERE #
        self.name = new_name

    def get_name(self):
        """
        Returns the user's current name
        """
        # YOUR CODE GOES HERE #
        return self.name

    def set_balance(self, amount):
        """
        Set the user's current balance to the given amount
        """
        # YOUR CODE GOES HERE #
        self.balance = amount

    def get_balance(self):
        """
        Returns the user's current balance
        """
        # YOUR CODE GOES HERE #
        return self.balance

    def add_balance(self, amount):
        """
        Add the given amount to the current balance
        """
        # YOUR CODE GOES HERE #
        self.balance += amount

    def last_purchase(self):
        """
        Return the user's most recent purchase
        """
        # YOUR CODE GOES HERE #
        return self.purchase_history.peek()

    def view_history(self):
        """
        Print the user's entire purchase history
        """
        # YOUR CODE GOES HERE #
        print(self.purchase_history)

    def view_cart(self):
        """
        Print all items in the user's cart
        """
        # YOUR CODE GOES HERE #
        print(self.cart)

    def clear_cart(self):
        """
        Remove all items from the user's cart
        """
        # YOUR CODE GOES HERE #
        self.cart = Queue()

    ##### Part 5.2 #####
    def add_cart(self, product_id):
        """
        Add the product with the given product id to the user's cart
        """
        # YOUR CODE GOES HERE #
        item = self.store.get_product(product_id)
        if item == None:
            pass
        else:
            self.cart.enqueue(item)

    def checkout(self):
        """
        Purchase all items in the user's cart and return a list of all
        purchased products.

        As soon as a product cannot be purchased, purchasing is stopped.
        Anything that was purchased successfully is returned in a list.
        """
        # YOUR CODE GOES HERE #
        purchases = []
        while not(self.cart.is_empty()):
            product = self.cart.peek()
            purchase = self.store.order(self.id, product.id)
            if purchase:
                self.cart.dequeue()
                purchases.append(purchase.product)
                self.purchase_history.push(purchase)
            else:
                break
        return purchases

    ##### Part 5.3 #####
    def undo_purchase(self):
        """
        Undo the user's most recent purchase.

        If there is no shopping history, print "USER: no purchase history" and
        do nothing else.
        Else, attempt to undo the purchase. If the store allows the request,
        remove that purchase from the user's purchase history.
        """
        # YOUR CODE GOES HERE #
        if self.purchase_history.is_empty():
            print("USER: no purchase history")
        else:
            last_purchase = self.purchase_history.peek()
            user = last_purchase.user
            user_id = user.id
            product = last_purchase.product
            request = self.store.undo_order(user_id, product)

            if request:
                user.purchase_history.pop()


class Premium_User(User):
    """
    Premium_User is a child class of User. Premium_User serves as an
    abstraction for users with special privileges. Premium users do not have to
    pay for shipping, are able to purchase special products, and have extra
    shopping privileges.
    """
    ##### Part 4.2 #####
    def __str__(self):
        """
        Returns the string representation as:
        "premium user: {name} - {balance}$"
        """
        # YOUR CODE GOES HERE #
        return "premium user: {} - {}$".format(self.name, self.balance)

    ##### Part 5.4 #####
    def buy_all(self, product_id):
        """
        The user will attempt to buy all available supply of a limited product.
        If the product is not a Limited Product, print
        "USER: not a limited product" and return an empty list.

        Else, purchase as many products as supply and user's balance allows.
        Return a list of all successful purchases.
        """
        # YOUR CODE GOES HERE #
        product = self.store.get_product(product_id)
        if isinstance(product, Limited_Product):
            for i in range(product.amount):
                self.add_cart(product_id)
            return self.checkout()

        else:
            print("USER: not a limited product")
            return []

    def undo_all(self):
        """
        Undoes all purchases in the user's purchase history until none is left.
        If a request is sent to undo a purchase of a Limited Product, that
        request will be ignored and this function stops.
        """
        # YOUR CODE GOES HERE #
        while True:
            last_purchase = self.purchase_history.peek()
            if self.purchase_history.is_empty(): break
            elif isinstance(last_purchase.product, Limited_Product):
                break
            self.undo_purchase()



#######################################################################
#                               STORE                                 #
#######################################################################
class Store:
    """
    Store class serves as abstraction for stores the users will shop at. Stores
    handle user registration, orders, and delivers/receives products from the
    warehouse.
    """
    ##### Part 4.3 #####
    def __init__(self, warehouse):
        """
        Constructor for Store instances. Each store is initialized with the
        warehouse they shipping products from. Instance attributes are their
        warehouse and a dictionary of all users using the store as user id,
        user instance key-value pairs.
        """
        # YOUR CODE GOES HERE #
        self.users = dict()
        self.warehouse = warehouse

    def __str__(self):
        """
        Return the string representation as:
        "STORE: store with {number of users} users and \
        {size of warehouse} products"
        """
        # YOUR CODE GOES HERE #
        return "STORE: store with {} users and {} products".format(
            len(self.users), 
            self.warehouse.size()
        )

    def get_product(self, product_id):
        """
        Returns the product associated with the given product_id from the
        warehouse.
        """
        # YOUR CODE GOES HERE #
        return self.warehouse.get_product(product_id)

    def view_products(self, sort=False):
        """
        Prints all products available in inventory in this format:

            ============================
            <ID> Product - Price
            <0> iphone - 399$
            <1> macbook air - 999$ (special)
            <2> free iphone - 0$ (10 left)
            ============================
        
        If sort is True, the products are sorted in ascending order based on
        their prices.
        """
        # YOUR CODE GOES HERE #
        products = self.warehouse.list_products()
        header = "============================"
        print(header)
        print("<ID> Product - Price")
        if sort:
            products = sorted(products, key=lambda x: x.price)

        for product in products:
            print(product)
        print(header)

    ##### Part 5.1 #####
    def add_user(self, user):
        """
        Adds the given user to the store's user dictionary and return True.
        If the given user is already in the dictionary, then print 
        "STORE: User already exists" and return False.
        """
        # YOUR CODE GOES HERE #
        if user.id in self.users:
            print("STORE: User already exists")
            return False
        self.users[user.id] = user

    ##### Part 5.2 #####
    def order(self, user_id, product_id):
        """
        The user with given the user id will attempt to order the product
        associated with the given product id.
        This order will only complete if:

            1. This store stocks the specified item. If not, print
            "STORE: Product not found" and return False.

            2. The user is buying products they are allowed to buy.
            Premium users have access to Special Products. If a regular user is
            trying to order a Special Product, print
            "STORE: Special product is limited to premium user" and return
            False.

            3. The user has enough money to purchase the product. Premium users
            only need to pay the product's price. Regular users pay the item
            price + shipping (1.1 * product price rounded down to nearest
            integer).
            If the user does not have enough money print:
            "STORE: Not enough money QQ" and return False

        If this order is successful:
            * the total price is subtracted from the user's balance
            * the ordered product is exported from the warehouse
            * "STORE: {user name} ordered {product name}. {user name} has \
            {user balance}$ left." is printed
            * A new payment history will be returned
        """
        user = self.users[user_id]
        product = self.get_product(product_id)

        find_price = lambda x: \
            x if isinstance(user, Premium_User) \
            else int(1.1 * x)
        price = find_price(product.price)
        if product == None:
            print("STORE: Product not found")
            return False
        elif not(isinstance(user, Premium_User)) and \
    isinstance(product, Special_Product):
            print("STORE: Special product is limited to premium user")
            return False
        elif user.get_balance() < price:
            print("STORE: Not enough money QQ")
            return False
        else:
            user.add_balance(-(price))
            self.warehouse.export_product(product_id)
            print("STORE: {0} ordered {1}. {0} has {2}$ left.".format(
                user.get_name(), 
                product.name, 
                user.get_balance()
                )
            )
            return History(product, user)


    ##### Part 5.3 #####
    def undo_order(self, user_id, product):
        """
        The store will attempt to undo a user's purchase. Refunds on Limited
        Products are not allowed and this message will be printed:
        "STORE: can’t refund Limited_Product"

        Else, the product's price will be refunded to the user's balance. Any
        shipping fee will not be refunded. After a successful refund
        "STORE: {user name} refunded {product name}. \
        {user name} has {user balance}$ left." will be printed and True will be
        returned.
        """
        # YOUR CODE GOES HERE #
        user = self.users[user_id]
        if isinstance(product, Limited_Product):
            print("STORE: can’t refund Limited_Product")
            return False
        user.add_balance(product.price)
        print("STORE: {0} refunded {1}. {0} has {2}$ left.".format(
                user.get_name(),
                product.name,
                user.get_balance()
            )
        )
        return True

    ##### Part 6 #####
    def so_rich(self, money):
        """
        Given a certain amount of money, the function will find the least
        possible amount of money leftover from buying products sold in this
        store.

        The user is assumed to be a Premium User, which means premium items
        are purchasable. Each time a Limited Product is purchased, that
        product's amount is decremented by 1 (the product's actual amount 
        attribute remains unchanged).

        Possible answers are within the range [0, money].
        """
        # YOUR CODE GOES HERE #

        # suppose you haven't seen any product yet
        # the only possible amount of money left is "money"
        # this is a set to record the possible money left
        left = set([money])

        # get products
        lst = self.warehouse.list_products()

        for product in lst:

            # a temporary set to save the updates of "left"
            # you don't want to modify the set you're iterating through
            tmp_left = set()

            for m in left:
                # update tmp_left
                if type(product) != Limited_Product:
                    new_left = m
                    while new_left >= 0:
                        tmp_left.add(new_left)
                        new_left = new_left - product.price
                else:
                    # handle limited product
                    new_left = m
                    curr_amount = product.amount
                    while new_left >= 0 and curr_amount >= 0:
                        tmp_left.add(new_left)
                        new_left = new_left - product.price
                        curr_amount -= 1
            left = tmp_left

        return min(left)
