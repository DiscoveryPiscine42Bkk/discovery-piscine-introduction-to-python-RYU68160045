
def add_one(a_number):
    """
    This function takes a number and adds 1 to its *local copy*.
    It does not affect the original variable passed to it.
    """
   
    a_number = a_number + 1

my_variable = 10

print(my_variable)

add_one(my_variable)

print(my_variable)