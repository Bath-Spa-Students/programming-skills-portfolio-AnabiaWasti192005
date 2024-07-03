#Write an if-elif-else chain that determines a person’s stage of life.
age = 100

if age < 2:
    print("The person is a baby.")
elif 2 <= age < 5:
    print("The person is a toddler.")
elif 5 <= age < 12:
    print("The person is a kid.")
elif 12 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 60:
    print("The person is an adult.")
else:
    print("The person is an elder.")


