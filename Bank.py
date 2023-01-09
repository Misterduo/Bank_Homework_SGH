class Customer:
    last_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f"Customer id: {self.id} {self.firstname} {self.lastname}"


class Account:
    last_id = 1000
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        #TODO add throwing exception when amount is invalid
        if amount <= 0:
            raise ValueError('Amount is invalid')
        self._balance += amount

    def charge(self, amount):
        #TODO add throwing exception when amount is invalid or there are insufficient funds
        if amount <= 0:
            raise ValueError('Amount is invalid')
        if self._balance - amount < 0:
            raise ValueError('Insufficient funds')
        self._balance -= amount

    def __repr__(self):
        return f'Account [{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        ##TODO implement
        ## 1. find both accounts
        ## 2. perform charge and deposit
        from_acc = self.find_account(from_account_id)
        to_acc = self.find_account(to_account_id)
        if from_acc is None:
            raise ValueError('Invalid "from" account')
        if to_acc is None:
            raise ValueError('Invalid "to" account')
        from_acc.charge(amount)
        to_acc.deposit(amount)

    def find_account(self, acc_id):
        # loop through the list of accounts and return the matching account
        for acc in self.account_list:
            if acc.id == acc_id:
                return acc
        return None

    def __repr__(self):
        return f'Bank:\n{self.customer_list}\n{self.account_list}\n----------'


class BankException(Exception):
    def __init__(self, msg, amount):
        super().__init__(msg)
        self.amount = amount




#c1 = Customer('John', "Smith")
b = Bank()
c1 = b.create_customer('John', 'Smith')
print(c1)
print(b)
a1 = b.create_account(c1)
#a = Account(c1)
print(a1)

try:
    a1.deposit(-200)  #ValueError (Negative)/Amount is invalid
except ValueError as ex:
    print(f'Error: {ex}')

try:
    a1.charge(-20)  #ValueError (Negative)/Amount is invalid
except ValueError as ex:
    print(f'Error: {ex}')

try:
    a1.charge(300)  #ValueError(Balance-Amount)/Insufficient funds
except ValueError as ex:
    print(f'Error: {ex}')

a2 = b.create_account(c1)
print('Before transfer')
print(b)

a_from = b.find_account(1001)
print('account from')
print(a_from)

try:
    b.transfer(2006, 2005, 10)  #ValueError(from_acc is None)/Invalid "from" account
except ValueError as ex:
    print(f'Error: {ex}')

print('After transfer')
print(b)
