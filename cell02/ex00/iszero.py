try:
    number = int(input("Please enter a number: "))

    if number == 0:
        print ("Thisnumber is equal to zero.")
    else:
        print("This number is different from zero.")

except ValueError:
    print("Invalid input . Please enter an integer.")