
import sys

args = sys.argv[1:]

#
num_args = len(args)


if num_args == 0:
  
    print("none")
else:
    
    print(f"parameters: {num_args}")
    
    for param in args:
        
        print(f"{param}: {len(param)}")