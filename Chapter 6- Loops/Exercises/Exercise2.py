#A movie theater charges different ticket prices depending on a person’s age.
while True :
    # Asking the users about their age
    age = input("Please enter your age (enter 'done' to exit): ")

    # If the user wants to exit
    if age.lower() == 'done':
        break

    # Converting the input to an integer
    age = int(age)

    # Displaying the ticket price based on the user age
    if age < 8:
        ticket_price = 5
    elif 8 <= age <= 19:
        ticket_price = 17
    else:
        ticket_price = 22

    # Printing the ticket price infront of the user
    print(f"Your movie ticket costs ${ticket_price}\n")

