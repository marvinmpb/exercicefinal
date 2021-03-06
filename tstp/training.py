#training.py

def calcul (x,y):
	return x + y

while True:
	x = float(input("select a number: "))
	y = float(input("Select an other number: "))
	result = x + y
	if result >= 100:
		print (result)
	else:
		print ("Wrong form")
	break



#question2
def supnum (num):
	previousnum = 0
	for i in range (num):
		sup = previousnum + i
		print ("current number", i, previousnum, "sup: ", sup )
		previousnum = i

print ("printing current and previous number sum in a given range (10)")
supnum (15)

#Question3
original = "pynative"
print (original [0])
print (original [2])
print (original [4])
print (original [6]) 


#question4
on_teste = "pynative"
print (on_teste [4:8])

#question5

print ("real list = [10, 20, 30, 40, 10]")
list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]
real_list = [10, 20, 30, 40, 10]
print (list1) == real_list
print (list2) == real_list

#question6


print ("Divisible of 5 in a list:")

a = 10
b = 20
c = 33
d = 46
e = 55

if a % 5 == 0:
	print (a)
if b % 5 == 0:
	print (b)
if c % 5 == 0:
	print (c)
if d % 5 == 0:
	print (d)
if e % 5 == 0:
	print (e)



numlist = [10, 20, 33, 46, 55]

def finddivisble (numlist):
	print ("given list is", numlist)
	print ("divisble of 5 in a list")
	for num in numlist:
		if (num%5 == 0):
			print (num)
finddivisble(numlist)

#question7
string = "emma is good developer. emma is a writer"
how_many = "emma"

count = string.count (how_many)
print ("the count is:", count)


#question8

#for num in range(10):
#    for i in range(num):
#        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
#    print("\n")

#fonctionne uniquement sur python3


#question11

numerolist = [7, 5, 3, 6]
def f():
	print (numerolist [-1])
	print (numerolist [-2])
	print (numerolist [-3])
	print (numerolist [-4])
	
f()




number = 7536
print("Given number", number)
while (number > 0):
    # get the last digit
    digit = number % 10
    
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end = " ")

print (end = '\n')

#question12

income = 45000
taxpayable = 0
print ("given income", income)

if income <= 10000:
	taxpayable = 0
elif income <= 20000:
	taxpayable = (income- 10000) *10 / 100
else:
	taxpayable = 0
	taxpayable = 10000 *10 / 100
	taxpayable += (income - 20000) * 20 / 100

print ("total tax to pay is", taxpayable)


#question13

for i in range (1, 11):
	for j in range (1, 11):
		print (i * j, end = " ")
	print ("\t\t")


#question14
rows = 5
b = 0
for i in range (rows, 0, -1):
	("b" + str(1))
	b = '*'
	for j in range (1, i + 1):
		print (b, end = ' ')

	print ('')


