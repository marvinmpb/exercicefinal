print ("hello !")

print "marvin"

print ("2+2")

x = 6

def f():
	global x
	x += 1
	print (x)

f ()

if __name__ == "__main__":
	print ("hello")

import statistics
z = [ 0, 2, 5, 26, 35, 42, 61, 85 ]
print statistics.median (z)