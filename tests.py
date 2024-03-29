"""Testing suite for compute_fraction.py"""
import unittest
import subprocess

class TestMainFunctionality(unittest.TestCase):
    def test_addition1(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '2/3', '+', '3/4'], capture_output=True, text=True)
        print("2/3 + 3/4 = 1_5/12")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '1_5/12')
    
    def test_addition2(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '1/3', '-', '17/8'], capture_output=True, text=True)
        print("1/3 + 17/8 = -1_19/24")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-1_19/24')
    
    def test_addition3(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-2/3', '+', '3/4'], capture_output=True, text=True)
        print("-2/3 + 3/4 = 1/12")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '1/12')
    
    def test_subtraction1(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '1/2', '-', '3/4'], capture_output=True, text=True)
        print("1/2 - 3/4 = -1/4")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-1/4')

    def test_subtraction2(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '1/2', '-', '7/4'], capture_output=True, text=True)
        print("1/2 - 7/4 = -1_1/4")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-1_1/4')

    def test_subtraction3(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-1_1/2', '-', '3_1/9'], capture_output=True, text=True)
        print("-1_1/2 - 3_1/9 = -4_11/18")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-4_11/18')

    def test_multiplication1(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-1_1/2', '*', '1/4'], capture_output=True, text=True)
        print("-1_1/2 * 1/4 = -3/8")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-3/8')

    def test_multiplication2(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-5/3', '*', '4/3'], capture_output=True, text=True)
        print("-5/3 * 4/3 = -2_2/9")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-2_2/9')

    def test_multiplication3(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-5/3', '*', '-4/3'], capture_output=True, text=True)
        print("-5/3 * 4/3 = 2_2/9")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '2_2/9')

    def test_division1(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-5/7', '/', '4/3'], capture_output=True, text=True)
        print("-5/7 / 4/3 = -15/28")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-15/28')

    def test_division2(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '-1_5/7', '/', '2_4/3'], capture_output=True, text=True)
        print("-1_5/7 / 2_4/3 = -36/70")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '-18/35')

    def test_division3(self):
        # Run the main script with command-line arguments and capture the output
        result = subprocess.run(['python', 'compute_fraction.py', '1_3/7', '/', '2/5'], capture_output=True, text=True)
        print("1_3/7 / 2/5 = 3_4/7")
        # Assert that the correct output is printed
        self.assertEqual(result.stdout.strip(), '3_4/7')

if __name__ == '__main__':
    unittest.main()