

def add (x, y):
	return x + y

def soustract (x,y):
	return x - y

def divid (x, y):
	return x / y

def multiply (x, y):
	return x * y

def modulo (x, y):
	return x%y

print ("select an operation")
print ("1. add")
print ("2. soustract")
print ("3. divid")
print ("4. multiply")
print ("5. modulo")
while True:
	choice = input ("enter choice (1/2/3/4/5): ")
	if choice in ("1", "2", "3", "4", "5"):
		num1 = float(input("Enter first number:"))
		num2 = float(input("Enter second number:"))

		if choice == "1":
			print (num1, "+", num2, "=", add (num1,num2))
		if choice == "2":
			print (num1, "-", num2, "=", soustract (num1,num2))
		if choice == "3":
			print (num1, "/", num2, "=", divid (num1, num2))
		if choice == "4":
			print (num1, "*", num2, "=", multiply (num1,num2))
		if choice == "5":
			print (num1, "%", num2, "=", modulo (num1,num2))
		break
	else:
		print ("invalid input")



