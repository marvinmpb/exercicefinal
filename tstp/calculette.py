def add (x,y):
	return x + y

def soustrac (x,y):
	return x - y

def mul (x,y):
	return x * y

def div (x,y):
	return x / y

print ("select operation")
print ("1.add")
print ("2.soustrac")
print ("3.mul")
print ("4.div")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", soustrac(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        break
    else:
        print("Invalid Input")
