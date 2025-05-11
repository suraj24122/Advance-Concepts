class bank_account:
    def __init__(self):
        self._balance = 0

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount

    def get_balance(self):
        return self._balance

#object
acc = bank_account()
acc.set_balance(2000)
print(acc.get_balance())