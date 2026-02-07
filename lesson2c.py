# a dictionary is a data type that store data interms of key-value pair
# It is introduced by use of curly braces{}
# The values stored insde a dictionary can be of any data type
# To access the values in a dictonary we use the keys


phonebook = {
    "Benson" : "2547123456789",
    "mary" : "254783534228",
    "stephen": "2547255526"
}
# Showing the entire dictionary
print(phonebook)
print(type(phonebook))

#printing Bensons number
print(phonebook["Benson"])

print("==========================================================")

player = {
    "name": "Messi",
    "age": 40,
    "teams": ["PSG", "Barcelona", "Argentina"],
    "children": 3,
    "residence": "US",
    "phone": (2547836645, 254363778, 73666353)
}

# printing Barcelona
print(player["teams"][1])

# printing Messi's second phone number
print(player["phone"][1])
