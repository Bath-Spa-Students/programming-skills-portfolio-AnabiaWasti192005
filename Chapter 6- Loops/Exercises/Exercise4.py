#Make a list called sandwich_orders and fill it with the names of various sandwiches.
# List of sandwich orders
sandwich_orders = ['Chicken', 'Cheese', 'Egg', 'Roast beef', 'Wrap', 'Seafood']

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Process each sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich order
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print all finished sandwiches
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)







