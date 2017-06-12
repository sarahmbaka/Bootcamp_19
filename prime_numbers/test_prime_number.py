import unittest
from prime_number import get_prime_numbers


class Test_Generate_prime_numbers(unittest.TestCase):
    def test_it_works(self):
        self.assertEqual(get_prime_numbers(43), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])

    def test_if_is_negative(self):
        self.assertEqual(get_prime_numbers(-10), 'Negatives or Zero not allowed')

    def test_if_is_zero(self):
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
