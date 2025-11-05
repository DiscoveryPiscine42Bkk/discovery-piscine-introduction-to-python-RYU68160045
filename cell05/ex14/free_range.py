
import sys

args = sys.argv[1:]


if len(args) != 2:
    
    print("none")
else:
    try:
        
        num1 = int(args[0])
        num2 = int(args[1])
        
        
        
        if num1 <= num2:
            
            result_list = list(range(num1, num2 + 1))
        else:
            
            result_list = list(range(num1, num2 - 1, -1))
        
        print(result_list)

    except ValueError:
        
        print("none")