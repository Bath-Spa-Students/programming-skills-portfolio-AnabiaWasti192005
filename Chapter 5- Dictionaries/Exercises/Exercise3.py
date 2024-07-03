#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 
glossary = {
"Control Flow": "Fundamental components of programming languages that developers can use to control the order in which are executed in a programme.",
 "Data Structures":"Are used to organize data. As well as processing, retrieveing and storing Data.",
 "Strings Concatination": "The operation of joining 2 strings together",
 "String": "A sequence of characters, either as a literal constant or some kind of variable",
 "Python Version": "Python Version consists of 3 versions: a major version, a minor version and a micro version",
}

for term, definition in glossary.items():
    print(f"{term}: {definition}")

new_terms = {
    'For loop': 'control flow statement for specifying iteration, which allows code to be executed repeatedly.',
    'Alert': 'displays a message to the user to display some information to users.',
    'Term': 'Programmers are allowed to employ them whenever they want to make a decision. .',
    'Print' : 'Prints the specified message to the screen or other standard output device.',
    'Data' : 'Data refers to any information that a computer can store in its programs.',
}   

glossary.update(new_terms)

for term, definition in glossary.items():
    print(f"{term}: {definition}")



