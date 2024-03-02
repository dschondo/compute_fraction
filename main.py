"""Censys Technical Challenge Fraction computation python file."""
import sys
import click
import math

# Error checking on the command line args
def error_check(args):
    if len(args) != 3:
        raise Exception("Invalid number of command line arguments")
    
    value1, operator, value2 = args

    if operator not in ['+', '-', '*', '/']:
        raise Exception("Invalid math operator, must be in the set ['+', '-', '*', '/']")
    
# Returns the sign of a number
def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

# Function used to turn the input value into an improper (or proper) fraction
# Returns a string representing the fraction value
def parse_frac(fraction):
    fraction_parts = str.split(fraction, sep='_')

    # If dealing with mixed number, get the whole number, numerator, denomiator to reduce it
    if len(fraction_parts) == 2:
        whole, frac = fraction_parts
        num, den = str.split(frac, sep='/')
        num = (int(num) + (abs(int(whole)) * int(den)))*sign(int(whole))
        return f"{num}/{den}"
    # Else return the original fraction value
    return fraction

# Gets frac1 and frac2 to have common denominators
# Returns a pair of (frac1, frac2)
def common_den(frac1, frac2):
    num1 = int(str.split(frac1, sep='/')[0])
    den1 = int(str.split(frac1, sep='/')[1])
    num2 = int(str.split(frac2, sep='/')[0])
    den2 = int(str.split(frac2, sep='/')[1])

    new_den = den1 * den2
    num1 = den2 * num1
    num2 = den1 * num2

    return (f"{num1}/{new_den}", f"{num2}/{new_den}")

# Performs the add or subtract operation on frac1 and frac2
# Returns the solution
def add_or_sub(frac1, frac2, operation):
    num1 = int(str.split(frac1, sep='/')[0])
    den = int(str.split(frac1, sep='/')[1])
    num2 = int(str.split(frac2, sep='/')[0])

    if operation == '+':
        new_num = num1 + num2
    else:
        new_num = num1 - num2
    return f"{new_num}/{den}"

def mult_or_div(frac1, frac2, operation):
    num1 = int(str.split(frac1, sep='/')[0])
    den1 = int(str.split(frac1, sep='/')[1])
    num2 = int(str.split(frac2, sep='/')[0])
    den2 = int(str.split(frac2, sep='/')[1])
    new_num, new_den = 0, 0
    if operation == '*':
        new_num = num1 * num2
        new_den = den1 * den2
    # need to use recirpricol of the second fraction for division
    elif operation == '/':
        new_num = num1 * den2
        new_den = den1 * num2
    
    return f"{new_num}/{new_den}"

# Returns the non simplified value of frac1 (operator) frac2
def compute_value(frac1, frac2, operation):
    if operation == '+' or operation == '-':
        frac1, frac2 = common_den(frac1,frac2)
        return add_or_sub(frac1, frac2, operation)
    else:
        return mult_or_div(frac1, frac2, operation)


# Returns the simplest form of the computed fraction
def reduce_frac(computed_val):
    num = int(str.split(computed_val, sep='/')[0])
    den = int(str.split(computed_val, sep='/')[1])
    whole = 0

    # first check to see if it is an improper fraction
    if abs(num) > den:
        whole = (abs(num) // den) * sign(num)
        num = abs(num) % den

    # simplify num and den using the gcd
    gcd = math.gcd(abs(num), den)
    num = num // gcd
    den = den // gcd

    # format return value appropriately
    if whole == 0:
        return f"{num}/{den}"
    elif num == 0:
        return f"{whole}"
    else:
        return f"{whole}_{num}/{den}"

# Reads from the command line a math problem in the form (num1 operation num2)
# Uses click library to handle command line arguments
# @click.command()
# @click.argument("value1", nargs=1, type=click.STRING, metavar="<First Fraction Value>")
# @click.argument("operation", nargs=1, type=click.Choice(['+','-','/','*']), metavar="<Math Operation>")
# @click.argument("value2", nargs=1, type=click.STRING, metavar="<Second Fraction Value>")
def main():
    args = sys.argv[1:]
    error_check(args)

    # extract values from command line arguments
    value1, operation, value2 = args

    # simplify input fraction values if necessary
    # print(value1, value2, operation)
    frac1 = parse_frac(value1)
    frac2 = parse_frac(value2)

    computed_val = compute_value(frac1, frac2, operation)
    simplified_frac = reduce_frac(computed_val)

    print(simplified_frac)
    return simplified_frac

if __name__ == "__main__":
    main()
    # try:
    #     main()
    # except Exception as e:
    #     # Handle the exception and print the error message
    #     print("Error:", e)