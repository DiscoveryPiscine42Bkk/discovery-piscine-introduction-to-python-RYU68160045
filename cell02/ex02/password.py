


correct_password = "Python is awesome"

try:
   
    user_input = str(input())
    
   
    if user_input == correct_password:
       
        print("ACCESS GRANTED")
    else:
       
        print("ACCESS DENIED")

except EOFError:
   
    print("ACCESS DENIED")