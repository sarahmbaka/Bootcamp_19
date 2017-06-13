import unittest
from oop import *

class Oop_Test(unittest.TestCase):
        """ this tests if the correct output is provided"""
        def test_oop1(self):
                b1= BankAccount(1000)
                b1.withdraw(500)
                self.assertEqual(500, b1.get_balance())
        """ this tests if the fixed desposit account is able to inherit from bank account"""
        def test_oop2(self):
                b = FixedDepositAccount(20,13)
                print (b.withdraw(15))
                self.assertEqual(b.withdraw(15),'Sorry, This is a Fixed Account', msg='Fixed Account Error')
        """ this tests if minimum Balance Account inherits properly from Bank Account"""
        def test_oop3(self):
               b2 = MinimumBalanceAccount(3000,1500)
               self.assertEqual(b2.withdraw(1700),'Sorry, minimum balance must be maintained.', msg='Minimum Balance Account Error')

if __name__ == '__main__':
    unittest.main()