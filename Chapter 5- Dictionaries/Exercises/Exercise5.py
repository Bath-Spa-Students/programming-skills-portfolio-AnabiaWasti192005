#Make several dictionaries, where each dictionary represents a different pet. 
Pet_A = {"animal": "Cat", "owner": "Fatima"}
Pet_B = {"animal": "Hamster", "owner": "Dua"}
Pet_C = {"animal": "Rabbit", "owner": "Javeria"}

animals = (Pet_A, Pet_B, Pet_C)

for pet in animals:
    print(f"Kind of animal: {pet['animal']}")
    print(f"Owner's Name: {pet['owner']}")





