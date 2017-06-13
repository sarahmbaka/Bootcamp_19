      
class BankAccount:
    """Creates an account with the given balance."""
    def __init__(self, initial_balance):
        
        self.money = initial_balance
        self.penalty = 0
        """Deposits the amount into the account."""
    def deposit(self, amount):
        
        self.money += amount
        return self.money
        """
        Withdraws the amount from the account. 
        """
    def withdraw(self, amount):
        
        self.money -= amount
        return self.money

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.money

"""Creates a minimumBalance account, one cannot withdraw beyond the minimum"""
class MinimumBalanceAccount(BankAccount):
    def __init__(self, initial_balance ,minimum_balance):
        super().__init__(initial_balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.money - amount < self.minimum_balance:
            return 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)
"""Creates a fixed account, one cannot withdraw before some months expire but with a maximum one year"""
class FixedDepositAccount(BankAccount):
    def __init__(self,initial_balance, fixed_months):
        super().__init__(initial_balance)
        self.fixed_months = fixed_months
        
    def withdraw (self,amount):
        if self.fixed_months !=0:
            return 'Sorry, This is a Fixed Account'
        else:
            BankAccount.withdraw(self,amount)



b = FixedDepositAccount(20,13)
print (b.withdraw(15))
b1= BankAccount(1000)
b1.withdraw(500)
print (b1.get_balance())
b2 = MinimumBalanceAccount(3000,1500)
print (b2.withdraw(1700))