#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
Budget = 50
Usb_stick_price = 6
num_usb_sticks = Budget // Usb_stick_price
remaining_budget = Budget % Usb_stick_price
print(f"The girl is able to purchase {num_usb_sticks} USB sticks.")
print(f"She goint to have £{remaining_budget} left.")

