def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start ,end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num):
            print(num)

print_narcis_numbers(1000, 5000)

#function names called didn't match the actual name of function, replaced them 
# in line 1,10,12,13 ':' was missing after declaration of each loop, this was added by me;
#in function is_narc: num_str == str(n) and num_digits == len(num_str) was invalid assignment, replaces == with =
#in function print_narcis_numbers there was no ',' between start and end, so added;
# sum_of-powers used *** which is not valid operation of power in python, replaced with **