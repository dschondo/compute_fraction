"""Censys Technical Challenge Fraction computation python file without the REST API."""
import sys
import fraction

# Error checking on the command line args
def error_check(args):
    if len(args) != 3:
        raise Exception("Invalid number of command line arguments.")
    
    operator = args[1]
    if operator not in ['+', '-', '*', '/']:
        raise Exception("Invalid math operator, must be in the set ['+', '-', '*', '/'].")

# Modifies fraction1 and fraction2 to have common denominators
def common_denominators(fraction1: fraction.Fraction, fraction2: fraction.Fraction):
    new_denominator = fraction1.denominator * fraction2.denominator
    fraction1.set_numerator(fraction1.numerator * fraction2.denominator)
    fraction2.set_numerator(fraction2.numerator * fraction1.denominator)
    fraction1.set_denominator(new_denominator)
    fraction2.set_denominator(new_denominator)

# Function that adds two fractions and returns a new Fraction object
def add_fractions(fraction1: fraction.Fraction, fraction2: fraction.Fraction):
    new_numerator = fraction1.numerator + fraction2.numerator
    denominator = fraction1.denominator
    computed_fraction = fraction.Fraction(f"{new_numerator}/{denominator}")
    return computed_fraction.reduce_fraction()

# Function that adds two fractions and returns a new Fraction object
def subtract_fractions(fraction1: fraction.Fraction, fraction2: fraction.Fraction):
    new_numerator = fraction1.numerator - fraction2.numerator
    denominator = fraction1.denominator
    computed_fraction = fraction.Fraction(f"{new_numerator}/{denominator}")
    return computed_fraction.reduce_fraction()

# Function that adds two fractions and returns a new Fraction object
def multiply_fractions(fraction1: fraction.Fraction, fraction2: fraction.Fraction):
    new_numerator = fraction1.numerator * fraction2.numerator
    new_denominator = fraction1.denominator * fraction2.denominator
    computed_fraction = fraction.Fraction(f"{new_numerator}/{new_denominator}")    
    return computed_fraction.reduce_fraction()

def compute_fraction(fraction1: fraction.Fraction, fraction2: fraction.Fraction, operation):
    if operation == '+':
        common_denominators(fraction1, fraction2)
        return add_fractions(fraction1, fraction2)
    elif operation == '-':
        common_denominators(fraction1, fraction2)
        return subtract_fractions(fraction1, fraction2)
    elif operation == '*':
        return multiply_fractions(fraction1, fraction2)
    elif operation == '/':
        fraction2.recipricate_fraction()
        return multiply_fractions(fraction1, fraction2)
    else:
        raise Exception("Invalid math operator, must be in the set ['+', '-', '*', '/'].")
   

# Reads from the command line a math problem in the form (num1 operation num2)
def main():
    # Extract arguments from the command line and checks for 3 inputs, and valid operation
    args = sys.argv[1:]
    error_check(args)
    value1, operation, value2 = args

    # Call the Function class constructor to get Function objects
    fraction1 = fraction.Fraction(value1)
    fraction2 = fraction.Fraction(value2)
    print(compute_fraction(fraction1, fraction2, operation))
    

if __name__ == "__main__":
    main()