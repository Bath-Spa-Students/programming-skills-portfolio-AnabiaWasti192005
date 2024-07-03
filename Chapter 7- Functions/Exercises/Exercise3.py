#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
def make_shirt(size, message):
    """Prints a summary of the shirt size and message."""
    print(f"A {size} shirt will have the message printed on: '{message}'")

# Call the function using positional arguments
make_shirt("large", "We're all made of stars!")

# Call the function using keyword arguments
make_shirt(size="Extra large", message="Coffee is my spirit animal")
