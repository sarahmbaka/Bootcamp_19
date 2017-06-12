import unittest
from prime_number import get_prime_numbers

"""
test_it_works confirms if the function gives the correct output

test_if_is_negative confirms if the number provided in a negative returns an error message

test_if_is_zero confirms if the number entered in zero and returns an error message

test_if_not_variable_type confirms if the variale type is int

test_if_list confirms if the output of the function is a list

"""
class Test_prime_numbers(unittest.TestCase):
    def test_it_works(self):
        self.assertEqual(get_prime_numbers(43), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])

    def test_if_negative(self):
        self.assertEqual(get_prime_numbers(-10), 'Negatives or Zero not allowed')

    def test_if_zero(self):
        self.assertEqual(get_prime_numbers(0), 'Negatives or Zero not allowed')

    def test_if_not_variable_type(self):
        self.assertRaises(ValueError, get_prime_numbers, 'ten')

    def test_if_list(self):
        try:
            assert type(get_prime_numbers(10)) is list
        except AssertionError:
            raise(AssertionError("Wrong type"))

    
if __name__ == '__main__':
    unittest.main()
