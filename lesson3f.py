#create a python program that is able to determine whether a number is an even or an odd number

number = int(input("Enter your number here: "))
if number %2 == 0:
    print("even")
else:
    print("odd")

#create a python program that is able to determine whether a person can donate blood based on the age an weight of a person. if the weight is> 50kgs and age is >18 they can donate else not possible

Age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))
if Age >=18 and weight > 50:
    print("Donate")
else:
    print("Dont donate")