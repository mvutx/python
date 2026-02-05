#python lists
# A list in python is a collection of items that are ordered in a certain way
# A list is introduced by the square brackets []
#the items of a list are stored inside of indexes. In programming we start counting from index zero(0). 
# Alist is nutable i.e the contents can be changed 

cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "Mclaren","Range"]

print(cars)
print(type(cars))

# Accessing items of a list 
print(cars[2])
print("The car on index four is:",cars[4])

#list slicing - This is creating a list from a bigger list 
print(cars[4:])


#printing from index zero to index three
print(cars[:4])

#printing from hiance to probox
print(cars[2:3])

#list-Mutability
# we use a function append to add an item at the end of a list 
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)


#we use the pop function to remove an item at the end of a list
cars.pop()
print(cars)

# we can use an index to add items to our lists 
cars[5]="Pajero"
print(cars)

# we can use the sort function in an alphabetical order
cars.sort()
print()
