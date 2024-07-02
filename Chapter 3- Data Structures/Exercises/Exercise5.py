#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
guests = ["Romesa", "Abrish", "Meerub"]
unavailable_person = "Abrish"
print(f"Sadly, {unavailable_person} can't make it to the party.\n")
new_guest = "Manahil"
guests.remove(unavailable_person)
guests.append(new_guest)
for guest in guests:
    invitation = f"Dear {guest},\n\nWe are pleased to invite you to that you have been invited to the upcoming dinner party held at our residence. We would be pleased if you were to come over and enjoy this relaxing eveing with us. Please inform us about if you are interested in attending\n\nyour_truly, Anabia Wasti"
    print(invitation)




