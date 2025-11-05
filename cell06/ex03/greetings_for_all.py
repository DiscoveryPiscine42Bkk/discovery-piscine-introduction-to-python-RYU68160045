
def greetings(name='noble stranger'):
    """
    Displays a welcome message.
    - Greets 'noble stranger' if no name is provided.
    - Shows an error if the argument is not a string.
    """
    if not isinstance(name, str):
        print("Error! That's not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)