"""Python file for fraction objects."""
import math

# Class for a fraction object
class Fraction:
    # Class constructor, checks for valid input and then makes fraction object
    def __init__(self, fraction):
        # Initialize object variables and temporary variables
        self.whole_number, self.numerator, self.denominator = 0, 0, 0
        self.parse_fraction(fraction)
    
    # Sets the fractions numerator
    def set_numerator(self, new_numerator):
        self.numerator = new_numerator
    
    # Sets the fractions denominator
    def set_denominator(self, new_denominator):
        self.denominator = new_denominator
    
    # Parse the fraction input and assign object variables
    def parse_fraction(self, fraction):
        # Get the whole number if the input was a mixed number
        whole, fraction_parts = fraction.split('_') if '_' in fraction else (None, fraction)
        # Get the numerator and denominator if the input has fraction parts
        numerator, denominator = fraction_parts.split('/') if '/' in fraction_parts else(None, None)
        # If the input was a whole number, assign it to the whole number temp variable
        if '_' not in fraction and '/' not in fraction:
            numerator = "1"
            denominator = "1"
        
        # Error checking on the input fraction
        self.fraction_error_check(whole, numerator, denominator)

        # Make the fraction improper rather than a mixed number
        if self.whole_number != 0 or self.whole_number is not None:
            self.numerator += abs(self.denominator * self.whole_number)
            self.numerator *= self.sign(self.whole_number)
            self.whole_number = 0
        
        # Fix the sign of the fraction to where the overall sign is reflected in the numerator
        self.numerator = abs(self.numerator) * (self.sign(self.numerator) * self.sign(self.denominator))
        self.denominator = abs(self.denominator)
    
    # Check the fraction to make sure it contains all valid components
    def fraction_error_check(self, whole, numerator, denominator):
        # Check that all numbers are valid integers or None
        if self.is_valid_input(whole) and self.is_valid_input(numerator) and self.is_valid_input(denominator):
            self.whole_number = int(whole) if whole is not None else 0
            self.numerator = int(numerator) if numerator is not None else None
            self.denominator = int(denominator) if denominator is not None else None
        else:
            raise Exception("Invalid fraction input. Please use one of the forms with only valid integers: 1_1/2, 1/2, 1.")

        # Check for 0 in the denominator
        if self.denominator == 0:
            raise Exception("Invalid fraction input. Please do not put 0 in the denominator of any fraction.")

    # Function for error checking the user input, makes sure the input is a valid number, or NoneType
    @staticmethod
    def is_valid_input(number: str) -> bool:
        if number is not None:
            if number.startswith('-'):
                number = number[1:]
            return number.isdigit()
        return True

    # Takes a fraction and returns the fractions as it's recipricol
    def recipricate_fraction(self):
        temp_numerator = self.numerator
        self.numerator = self.denominator
        self.denominator = temp_numerator
    
    # Reduces the fraction into the simplest form
    def reduce_fraction(self):
        # First check to see if the fraction is improper
        self.whole_number = 0
        if abs(self.numerator) > self.denominator:
            self.whole_number = (abs(self.numerator) // self.denominator) * self.sign(self.numerator)
            self.numerator = abs(self.numerator) % self.denominator
        
        # If the numerator is now 0, the answer will be a whole number
        if self.numerator == 0:
            self.numerator = None
            self.denominator = None
        # Simplify numerator and denominator using the gcd if the answer is not a whole number
        else:
            gcd = math.gcd(abs(self.numerator), self.denominator)
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        return self

    # Returns the sign of a number
    @staticmethod
    def sign(number):
        if number >= 0:
            return 1
        return -1
    
    # Manage how the fraction is printed
    def __str__(self):
        if self.numerator == 0:
            return f"0"
        elif self.whole_number == None or self.whole_number == 0:
            return f"{self.numerator}/{self.denominator}"
        elif self.numerator == None:
            return f"{self.whole_number}"
        return f"{self.whole_number}_{self.numerator}/{self.denominator}"

        

    
            