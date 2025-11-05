
while True:
    try:
        
        user_input = input()
        
        
        if user_input == "STOP":
            
            break
    
        print("I got that! Anything else?")
    except EOFError:
        break