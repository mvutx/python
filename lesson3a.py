# Boolean -this is a data type evaluates either to true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidloan = True
print(paidloan)
print(type(paidloan))

# comparison operators : They are used to compare twoor more statements and usually return a boolean answer


number1 = 2
number2 = 5

print("is number1 greater than number2? ", number1 > number2)
print("is number1 less than number2? ", number1 < number2)
print("is number1 greater than or eaquals to number2? ", number1 >= number2)
print("is number1 less than or eaqual to number2? ", number1 <= number2)
print("is number1 eaqual to number2? ", number1 == number2)
print("is number1 not eaqual to number2? ", number1 != number2)

# Logical opertors 
#logical AND
# it returns true if an only if the condition/statement evaluates to true
print((3 > 1) and (7 > 6))

#logical or 
# It evaluates to true if one of the statements or condition is true 
print((3 > 1) or (7 < 6))

#Logical not 
#it is used to negate a statement/condition if the statement is true it becomes negated to false
print( not(90 > 70))