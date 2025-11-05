import sys

params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    
    for arg in reversed(params):
        print(arg)