

try:

    age_str = input("Please tell me your age: ")
   
    age_int = int(age_str)
    
    print(f"In 10 years, you'll be {age_int + 10} years old.")
    print(f"In 20 years, you'll be {age_int + 20} years old.")
    print(f"In 30 years, you'll be {age_int + 30} years old.")

except (ValueError, EOFError):
  
    pass