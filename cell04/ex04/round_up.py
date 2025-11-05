
import math

try:
    
    number_str = input("Give me a number: ")
    
    
    number_float = float(number_str)
    
    
    rounded_up_value = math.ceil(number_float)
    
    final_result = int(rounded_up_value)
    
    print(final_result)

except ValueError:
    
    print("That is not a valid number.")
except EOFError:
    
    pass