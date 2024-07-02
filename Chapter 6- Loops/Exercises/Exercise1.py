#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
pizza_toppings = []

while True:
    #  To select the user's topping
    topping = input("Enter a pizza topping (type 'Done' to finish): ")

    # If user went to finish
    if topping.lower() == 'done':
        break  

    # Adding the desired topping on
    pizza_toppings.append(topping)

    # Displaying a message saying(adding topping wbe adding toppings to their pizza
    print(f"Adding {topping} to your pizza.")

#  Final topping varieties
print("Your Desired pizza toppings:")
for topping in pizza_toppings:
    print(topping)











