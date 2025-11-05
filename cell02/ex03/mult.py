try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    if result > 0:

        print("The result is positive.",result)
    elif result < 0:

        print("The result is negative.",result)
    else:
        print ("The result is negative and positive.", result)
except (ValueError, EOFError):
    pass