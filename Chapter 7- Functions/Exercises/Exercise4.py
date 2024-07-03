#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
def make_shirt(size="medium", message="Oh la la"):
    """Prints a summary of the shirt size and message."""
    print(f"A {size} shirt will be printed with the message: '{message}'")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="Large", message="Keep Calm and Shine On")


