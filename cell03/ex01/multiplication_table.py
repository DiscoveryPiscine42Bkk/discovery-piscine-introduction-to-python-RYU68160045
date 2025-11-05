

try:
    
    base_number = int(input("Enter a number "))
    
    
    i = 0
    
    while i < 10:
        
        result = i * base_number
        
       
        print(f"{i} x {base_number} = {result}")
        
        
        i = i + 1

except (ValueError, EOFError):
    
    pass