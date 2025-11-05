
try:
    
    number_str = input("Give me a number: ")
  
    number_float = float(number_str)
    
    if number_float.is_integer():
        
        print("This number is an integer.")
    else:
        
        print("This number is a decimal.")

except ValueError:
    
    print("That is not a valid number.")
except EOFError:
    
    pass