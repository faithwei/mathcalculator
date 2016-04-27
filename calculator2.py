def add(num1, num2):
	return num1 + num2
# print add(4,5)

def subtract(num1, num2):
	return num1 - num2
# print subtract(1,2)

def multiply(num1, num2):
	return num1 * num2
# print multiply(1,2)

def divide(num1, num2):
	return num1 / num2
# print divide(1,2)

def modulo(num1, num2):
	return num1% num2
# print modulo(9,4)

def power(base, exponent):
	return base** exponent
# print power(3,3)

def square(base):
	exponent = 2
	return base** exponent
# print square(3)

	
print add(add(4,5) , subtract (9,6))
print subtract(divide(12,2) , 60)
print add(add (1,2) , 3)
print square(add (1,2))
print divide(modulo(3,4), multiply(9,9))
print multiply(7, add(3,8))
print subtract(add(1,2), multiply(3, add(4,5)))
print power(3, add(2,3))