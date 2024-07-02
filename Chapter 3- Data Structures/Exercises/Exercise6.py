#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
guests = ("Romesa", "Manahil", "Meerub")
print("Guess I must have 2 people over now")
invited_guests = guests[:2]
for guest in guests[2:]:
    print(f"I'm truly sorry, {guest}, Due to some inconviences, I must have 2 people over now. So you can't be invited.")
for guest in invited_guests:
    print(f"{guest}, Your still on the guest list.")
guests = ()
print("My guest list is now empty:", guests)








