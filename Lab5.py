import json

#customer class
class Customer:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        return json.dumps({
        "user_id": self.user_id,
        "first_name": self.first_name,
        "last_name": self.last_name
    })

#account class
class Account:
    def __init__(self, first_account, balance):
        self.first_account = first_account
        self.balance = balance
        
    def to_json(self):
        return json.dumps({
        "account_id": self.first_account,
        "balance": self.balance
    })

#bank class
class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, user_id, first_name, last_name):
        self.customers.append(Customer(user_id, first_name, last_name))

    def add_account(self, account_id, balance):
        self.accounts.append(Account(account_id, balance))

    def to_json(self):
        customers_json = [customer.to_json() for customer in self.customers]
        accounts_json = [account.to_json() for account in self.accounts]
        return json.dumps({
            "customers": customers_json,
            "accounts": accounts_json
        }, indent=4)

#instantiating customer, account, and bank objects
john = Customer(1, "John", "Smith")
jane = Customer(2, "Jane", "Doe")
john_account = Account(1, 5000)
jane_account = Account(2, 15000)
the_bank = Bank()

the_bank.add_customer(1, "John", "Smith")
the_bank.add_customer(2, "Jane", "Doe")
the_bank.add_account(1, 5000)
the_bank.add_account(2, 15000)

#printing json representation
print(john.to_json())
print(john_account.to_json())
print(the_bank.to_json())
