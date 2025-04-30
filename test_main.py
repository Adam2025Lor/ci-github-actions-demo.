import unittest
from main import my_function  # Import the function from main.py


class TestMyFunction(unittest.TestCase):
    def test_return_value(self):
        # Test input
        test_input = ["apple", "banana", "cherry"]

        # Call the function and capture the output
        result = my_function(test_input)

        # Check if the returned list matches the input
        self.assertEqual(result, test_input)


if __name__ == '__main__':
    unittest.main()
