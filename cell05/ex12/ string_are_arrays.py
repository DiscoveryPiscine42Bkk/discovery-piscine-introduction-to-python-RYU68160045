
import sys

#
args = sys.argv[1:]

#
num_args = len(args)


if num_args != 1:
    
    print("none")
else:
    
    the_string = args[0]
    
    if 'z' in the_string:
        
        print("z")
    else:
        
        print("The character z is not found in this string")