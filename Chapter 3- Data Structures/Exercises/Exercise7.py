#Think of at least five places in the world you’d like to visit.
#  Store the locations in a list
places_to_visit = ["Japan", "New York City, USA", "France", "Korea", "Italy"]

# Rearaange you list in it's original order.
print("Original order:", places_to_visit)

# Change your list to in a proper Alphabetical order
print("Alphabetical order:", sorted(places_to_visit))

# by printing your list, you can show the original order of your list.
print("Original order:", places_to_visit)

# print out your list in a reverse alphabetical order. Do not change the original list's order .
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Print out your list again to show it is indeed in the original order
print("Original order:", places_to_visit)

#  change the order of your list with the help of reverse. Then print the list to show that it's order has changed.
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

#  With the help of reverse, change the order of your list again. Then print the list to show it’s original order has returned.
places_to_visit.reverse()
print("Original order:", places_to_visit)

# With sort() change your list to store it in an alphabetical order. You must print the list to show that its order has been changed.
places_to_visit.sort()
print("Sorted in alphabetical order:", places_to_visit)

# With the help of sort() change your list to store it in reverse alphabetical order. You must print the list to show that its order has been changed.
places_to_visit.sort()
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places_to_visit)