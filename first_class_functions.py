"""
Code to demonstrate passing functions
"""

def is_even(n):
    """Function that checks if a number is even."""
    return n % 2 == 0

def is_greater_than_10(n):
    """Function that checks if a number is greater than 10"""
    return n > 10

def filter_list(lst, function):
    """Filter a list based on a criteria from a function"""
    
    return [item for item in lst if function(item)]

if __name__ == "__main__":

    numbers = [1, 4, 7, 10, 14, 17, 20]

    # Filter the even numbers
    print(filter_list(numbers, is_even))

    # Filter the numbers greater than 10
    print(filter_list(numbers, is_greater_than_10))

