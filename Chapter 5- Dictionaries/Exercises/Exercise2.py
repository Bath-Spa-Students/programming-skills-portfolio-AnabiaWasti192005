#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
programming_glossary = {
 "Control Flow": "Fundamental components of programming languages that developers can use to control the order in which are executed in a programme.",
 "Data Structures":"Are used to organize data. As well as processing, retrieveing and storing Data.",
 "Strings Concatination": "The operation of joining 2 strings together",
 "String": "A sequence of characters, either as a literal constant or some kind of variable",
 "Python Version": "Python Version consists of 3 versions: a major version, a minor version and a micro version",
}

# Print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")










