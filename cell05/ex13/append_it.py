
import sys

args = sys.argv[1:]
if not args:
  
    print("none")
else:
    
    for param in args:
        
        if not param.endswith("ism"):
            
            print(f"{param}ism")
            