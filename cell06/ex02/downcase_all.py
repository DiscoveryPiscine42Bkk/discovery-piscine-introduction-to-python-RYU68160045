import sys

def downcase_it(input_string):
    """
    Takes a string as an argument and returns it in lowercase.
    """
    return input_string.lower()

if len(sys.argv) == 1:
    print("none")
else:
   
    for arg in sys.argv[1:]:
        print(downcase_it(arg))