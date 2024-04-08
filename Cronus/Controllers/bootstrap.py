from Cronus.App.Models.ACCOUNT import Account
import random


class Bootstrap:
    def __init__(self, client):
        self.client = client

    def bootstrap(self):
        account = Account(self.client)

        random_number = random.randint(0, 100)
        account.message(f"Hello-{random_number}")
