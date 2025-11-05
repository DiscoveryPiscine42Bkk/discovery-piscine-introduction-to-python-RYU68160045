
import sys


try:
    num_params = len(sys.argv)
    
    
    if num_params == 2:
        
        parameter = sys.argv[1]
        
        
        answer = input("What was the parameter? ")
        
        
        if answer == parameter:
            print("Good job!")
        else:
            print("Nope, sorry.")
            
    else:
        
        print("none")

except EOFError:
   
    print("\nNope, sorry.") 