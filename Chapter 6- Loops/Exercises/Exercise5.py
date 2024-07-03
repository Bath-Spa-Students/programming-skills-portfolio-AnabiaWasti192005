#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# List of sandwich orders
sandwich_orders = ['Chicken', 'Cheese', 'Egg', 'Roast beef', 'Wrap', 'Seafood']

# Ensure 'CHicken' appears at least three times
sandwich_orders += ['Chicken', 'Chicken', 'Chicken']

# Dsiplay message about Seafood out of stock
print("Sorry, Seafood sandwiches are out of stock.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'Roast beef' in sandwich_orders:
    sandwich_orders.remove('Roast beef')

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Function to display current orders
def display_current_orders():
    print("\nCurrent Sandwich Orders:")
    for order in sandwich_orders:
        print(order)

# Initial prompt to add sandwich orders
print("\nWelcome to the Sandwich Shop!")

while sandwich_orders:
    # Process each sandwich order
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich order
    if current_sandwich != 'pastrami':
        print(f"I made your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)
    else:
        print("Apologies, no pastrami sandwiches available.")

# Print all finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)












