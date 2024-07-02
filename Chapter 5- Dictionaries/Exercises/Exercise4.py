#Make a dictionary containing three major rivers and the country each river runs through.
rivers = {"Zambezi": "Africa", "Ganges": "India", "Amazon river": "South America"}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)






