#chapitre9

import os 
os.path.join ("Users",
	          "Marvin",
	          "st.txt")

st = open ("st.txt", "w")
st.write ("Hi from Python !")
st.close ()

with open ("st.txt", "w") as f:
	f.write ("Hi from Python")

with open ("st.txt", "r") as f:
	print (f.read())

my_list = list ()

with open ("st.txt", "r") as f:
	my_list.append (f.read())

print (my_list)

import csv


with open("st.csv", "wb") as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one",
                    "two",
                    "three"])
    write.writerow(["four",
                    "five",
                    "six"])

import csv 
with open ("st.csv", "r") as f:
	r = csv.reader (f, delimiter = ",")
	for row in r:
		print (",".join (row))


#Question1
with open ("st.txt", "r") as m:
	print (m.read())


#Question2
answer = input ("What's your name ?")
with open ("fav_color.txt", "w") as f:
	f.write (answer)


#Question3

import csv 

movies = [['Top Gun', 'Risky Business', 'Minority Report', 'Titanic', 'The Revenant', 'Inception','Training Day', 'Man on Fire', 'Flight']]
with open ("movies.csv", "w") as csvfile:
	spamwriter = csv.writer (csvfile, delimiter= ",")
	for movie_list in movies:
		spamwriter.writerow (movie_list) 






#Chapitre10


def hangman (exemple):
	wrong = 0
	stages = ["",
	         "________                ",
	         "|                       ",
	         "|        |              ",
	         "|        O              ",
	         "|       /|\             ",
	         "|       / \             ",
	         "|                       "
	         ]
	rletters = list(exemple)
	board = ["_"] * len(exemple)
	win = False
	print ("Welcome to Hangman")

	while wrong < len(stages) -1: 
		print ("\n")
		msg = "Guess a letter"
		char = input (msg)
		if char in rletters:
			cind = rletters.index (char)
			board[cind] = char
			rletters [cind] = "$"
		else:
			wrong += 1
		print (("".join (board)))
		e = wrong +1
		print ("\n".join(stages[0:e]))
		if "_" not in board:
			print ("You win !")
			print ("".join(board))
			win = True
			break
	if not win:
		print ("\n".join (stages [0:wrong]))
		print ("You lose ! It was {}.".format (exemple))

hangman ("cat")




#chapitre12

x = 2
y = 4
z = 8
xyz = x + y + z
print (xyz)

rock = []
country = []

def collect_song ():
	song = "enter a song: "
	ask = "type r or c. q to quit "

	while True:
		genre = input (ask)
		if genre == "q":
			break

		if genre == "r":
			rk = input (song)
			rock.append (rk)

		elif genre == "c":
			cy = input (song)
			country.append (cy)

		else:
			print ("Invalid.")
	print (rock)
	print (country)

collect_song ()

class Orange:
	def __init__ (self):
		print ("Created !")

Orange ()

class Orange:
	def __init__ (self, w, c):
		self.weight = w
		self.color = c
		print ("Created !!")


or1 =  Orange (25, 'brown')
print (or1)

class Orange:
	def __init__ (self, w, c):
		self.weight = w
		self.color = c
		print ("Created !")

or1 = Orange(10, "Dark orange")
print (or1.weight)
print (or1.color)


class Marvin:
	def __init__ (self, w, c, p, s):
		self.weight = w
		self.color = c
		self.power = p
		self.speed = s
		print ("Marvin has just been created !!")
mar = Marvin (185, "Brown", 99, "Very fast 99"  )
print (mar.weight) 
print (mar.color)
print (mar.power)
print (mar.speed)


class Orange: 
	def __init__ (self, w, c):
		self.weight = w
		self.color = c
		print ('Created !')

or1 = Orange (10, 'Dark Orange')
or1.weight = 100
or1.color = 'Light Orange'

print (or1.weight)
print (or1.color)


class Orange:
	def __init__ (self, w, c):
		self.weight = w
		self.color = c
		print ("Created !")

or1 = Orange (4, "light orange")
or2 = Orange (8, "dark orange")
or3 = Orange (14, "yellow")

class Orange ():
	def __init__ (self, w, c ):
		"""weight are in oz"""
		self.weight = w
		self.color = c
		self.mold = 0
		print ("Created !")
	def rot (self, days, temp):
		self.mold = days * temp

orange = Orange (6, "orange")
print (orange.mold)
orange.rot (10, 98)
print (orange.mold)


class Rectangle ():
	def __init__ (self, w, l):
		self.width = w
		self.len = l

	def area (self):
		return self.width * self.len

	def change_size (self, w, l):
		self.width = w
		self.len = l

rectangle = Rectangle (10, 20)
print (rectangle.area ())
rectangle.change_size (20, 40)
print (rectangle.area())

class Juliette:
	def __init__ (self, h, sz, s):
		self.hair = h
		self.size = sz
		self.skin = s
		print ("Juliette has been Created !")

a1 = Juliette ('Black', 1.66, 'white')
print (a1.hair)
print (a1.size)
print (a1.skin)

#exercice
#question1

class Apple:
	def __init__ (self, c, w, t, s):
		self.color = c
		self.weight = w
		self.taste = t
		self.size = s
		print ("Apple has been created")

a1 = Apple ("Green", '7', 'Juicy', 'Small')
print (a1.color)
print (a1.weight)
print (a1.taste)
print (a1.size)

#question2

import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.area())

print (math.pi)

#question3

class Triangle:
	def __init__ (self, s, l):
		self.side = s
		self.long = l
		print ('Triangle is create')

	def area (self):
		return self.side * self.long / 2

triangle = Triangle (20, 30)
print (triangle.area())



#question4

class Hexagon ():
	def __init__ (self, s1, s2, s3, s4, s5, s6):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.s4 = s4
		self.s5 = s5
		self.s6 = s6

	def perimeter (self):
		return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon (1, 2, 3, 4, 5, 6)
print (a_hexagon.perimeter ())



#chapitre13

class Rectangle():
	def __init__ (self, w, l):
		self.width = w
		self.len = l 

	def area (self):
		return self.width * self.len 

class Data:
	def __init__ (self):
		self.nums = [1, 2, 3, 4, 5]

	def change_data (self, index, n ):
		self.nums [index] = n

data_one = Data ()
data_one.nums [0] = 100
print (data_one.nums)

data_two = Data ()
data_two.change_data (0, 100)
print (data_two.nums)

class PublicPrivateExample:
	def __init__ (self):
		self.public = "safe"
		self._unsafe = "unsafe"

#	def public_method (self):
		# clients can use this pass

#	def _unsafe_method (self):
        # clients shouldn't use this pass

print ('Hello, World !')
print (200)
print (200.1)

print (type ("Hello world"))
print (type (200))
print (type (200.1))

class Shape ():
	def __init__ (self, w, l):
		self.width = w
		self.len = l

	def print_size (self):
		print ("""{} by {} 
			   """.format (self.width,
			   	           self.len))

my_shape = Shape (20, 25)
my_shape.print_size ()



class Square (Shape):
	pass

a_square = Square (20, 20)
a_square.print_size ()


class Shape ():
	def __init__ (self, w, l):
		self.width = w
		self.len = l

	def print_size (self):
		print ("{} by {}".format (self.width, self.len))


class Square (Shape):
	def area (self):
		return self.width * self.len

a_square = Square (20, 20)
print (a_square.area ())

class Shape ():
	def __init__ (self, w, l):
		self.width = w
		self.len = l

	def print_size (self):
		print (" {} by {}".format (self.width, self.len))

class Square (Shape):
	def area (self):
		return self.width * self.len 

	def print_size (self):
		print ("I am {} by {}".format (self.width, self.len))

a_square = Square (20, 20)
a_square.print_size ()

class Dog ():
	def __init__ (self,
		         name,
		         breed,
		owner):
	    self.name = name
	    self.breed = breed
	    self.owner = owner

class Person ():
	def __init__ (self, name):
		self.name = name

mick = Person ("Mick Jagger")
stan = Dog ("Stanley",
	        "Bulldog",
	        mick)
print (stan.owner.name)

#question1

class Rectangle ():
	def __init__ (self, l, j):
		self.longueur = l
		self.largeur = j 

	def calculate_perimeter (self):
		return self.longueur * 2 + self.largeur * 2

class Square:
	def __init__ (self, s):
		self.square = s

	def calculate_perimeter (self):
		return self.square * 4

a_rectangle = Rectangle (4, 5)
print (a_rectangle.calculate_perimeter ())

a_square = Square (5)
print (a_square.calculate_perimeter ())

#question2

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(10)
print(a_square.s1)

a_square.change_size(-4)
print(a_square.s1)





#question2 avec la méthode input 
class Square:
	def __init__ (self, s):
		self.square = s

	def calculate_perimeter (self):
		return self.square * 4

	def change_size (self):
		choice = input ("Choice addition '1' ou soustraction '2': ")
		choice = int (choice)
		if choice == 1:
			self.square +=1
			return self.square * 4
		if choice == 2:
			self.square -=1
			return self.square * 4

a_square = Square (5)
print (a_square.change_size ()) 


#question3
class Shape ():
	def what_am_i (self):
		print ("I am a shape.")

		
class Rectangle (Shape):
	def __init__ (self, l, j):
		self.longueur = l
		self.largeur = j 

	def calculate_perimeter (self):
		return self.longueur * 2 + self.largeur * 2

class Square (Shape):
	def __init__ (self, s):
		self.square = s

	def calculate_perimeter (self):
		return self.square * 4

a_rectangle = Rectangle (20, 50)
a_square = Square (29)

a_rectangle.what_am_i ()
a_square.what_am_i ()

#question4
class Rider ():
	def __init__ (self, name):
		self.name = name

class Horse ():
	def __init__ (self, name, rider):
		self.name = name
		self.rider = rider 

the_rider = Rider ("Sally")
harry_the_horse = Horse ("Harry", the_rider)

print ("The name of Horse is {}".format (harry_the_horse.name))
print ("The name of Rider is {}".format (harry_the_horse.rider.name))






#chapitre14

class Square:
	pass

print (Square)

class Rectangle ():
	def __init__ (self, w, l):
		self.width = w
		self.len = l

	def print_size (self):
		print ("{} by {}".format (self.width, self.len))

my_rectangle = Rectangle (10, 24)
my_rectangle.print_size ()

class Rectangle ():
	recs = []

	def __init__ (self, w, l):
		self.width = w
		self.len = l
		self.recs.append ((self.width, self.len))

		def print_size (self):
			print ("{} by {}".format (self.width, self.len))

r1 = Rectangle (10, 24)
r2 = Rectangle (20, 40)
r3 = Rectangle (100, 200)
r4 = Rectangle (400, 800)

print (Rectangle.recs)


class Lion:
	def __init__ (self, name):
		self.name = name

lion = Lion ("Dilbert")
print (lion)

class Lion:
	def __init__ (self, name):
		self.name = name

	def __repr__ (self):
		return self.name

lion = Lion ("Dilbert")
print (lion)

class AlwwaysPositive:
	def __init__ (self, number):
		self.n = number

	def __add__ (self, other):
		return abs (self.n + other.n)

x = AlwwaysPositive (-20)
y = AlwwaysPositive (10)
print (x + y)

class Person:
	def __init__ (self):
		self.name = "Bob"

bob = Person ()
same_bob = bob
print (bob is same_bob)

another_bob = Person ()
print (bob is another_bob)


x = 10
if x is None:
	print ("x is None")
else:
	print ("x is not None")

x = None
if x is None:
	print ("x is None")
else:
	print ("x is not None")



#question1
class Square ():
	add = []

	def __init__ (self, s):
		self.square = s
		self.add.append ((self.square * 4))

	def calculate_perimeter (self):
		return self.square * 4

s1 = Square (5)
s2 = Square (8)
print (Square.add)
# ----------------

class Shape ():
	def what_am_i (self):
		print ('I am a shape.')

class Square (Shape):
	square_list = []

	def __init__ (self, s):
		self.square = s
		self.square_list.append (self)

	def calculate_perimeter (self):
		return self.square * 4

	def what_am_i (self):
		super ().what_am_i ()
		print ("I am a Square.")

a_square = Square (29)
print (Square.square_list)
another_square = Square (93)
print (Square.square_list)


#question2
class Shape ():
	def what_am_i (self):
		print ('I am a shape.')

class Square (Shape):
	square_list = []

	def __init__ (self, s):
		self.square = s
		self.square_list.append (self)

	def calculate_perimeter (self):
		return self.square * 4

	def what_am_i (self):
		super ().what_am_i ()
		print ("I am a Square.")

	def __repr__ (self):
		return "{} by {} by {} by {}".format (self.square, self.square, self.square, self.square)

a_square = Square (29)
print (a_square)

# ------------- 


class Square ():

	def __init__ (self, s):
		self.square = s
		
	def calculate_perimeter (self):
		return self.square * 4

	def print_size (self):
		print ("{} by {}".format (self.square, self.square))

a_square = Square (10)
a_square.print_size ()
a_square = Square (30)
a_square.print_size ()

#question3

def essai (x, z):
	return x is z
	
print ('x' is 'z')
print ('x' is not 'z')




#chapitre15

class Card:
	suits = ("Spades", "hearts", "diamonds", "clubs")

	values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

	def __init__ (self, v, s):
		"suit + value are ints"
		self.value = v
		self.suit = s

	def __lt__ (self, c2):
		if self.value < c2.value:
			return True
		if self.value == c2.value:
			if self.suit < c2.suit:
				return True
			else:
				return False
		return False

	def __gt__ (self, c2):
		if self.value > c2.value:
			return True
		if self.value == c2.value:
			if self.suit > c2.suit:
				return True
			else:
				return False
		return False

	def __repr__ (self):
		v = self.values [self.value] + " of " + self.suits [self.suit]
		return v

#card1 = Card (10, 2)
#card2 = Card (11, 3)
#print (card1 < card2)

#card1 = Card (10, 2)
#card2 = Card (11, 3)
#print (card1 > card2)

#card = Card (4, 2)
#print (card)

from random import shuffle

class Deck:
	def __init__ (self):
		self.cards = []
		for i in range (2, 15):
			for j in range (4):
				self.cards.append (Card (i, j))
		shuffle (self.cards)

	def rm_card (self):
		if len (self.cards) == 0:
			return
		return self.cards.pop ()

deck = Deck ()
for card in deck.cards:
	print (card)

class Player:
	def __init__ (self, name):
		self.wins = 0
		self.card = None 
		self.name = name

class Game:
	def __init__ (self):
		name1 = input ("p1 name ")
		name2 = input ("p2 name ")
		self.deck = Deck ()
		self.p1 = Player (name1)
		self.p2 = Player (name2)

	def wins (self, winner):
		w = "{} wins this round"
		w = w.format (winner)
		print (w)

	def draw (self, p1n, p1c, p2n, p2c):
		d = "{} drew {} {} drew {}"
		d = d.format (p1n, p1c, p2n, p2c)
		print (d)

	def play_game (self):
		cards = self.deck.cards
		print ("beginning War !")
		while len (cards) >= 2:
			m = "q to quit. Any " + "key to play:"
			response = input (m)
			if response == "q":
				break
			p1c = self.deck.rm_card ()
			p2c = self.deck.rm_card ()
			p1n = self.p1.name
			p2n = self.p2.name
			self.draw (p1n, p1c, p2n, p2c)
			if p1c > p2c:
				self.p1.wins += 1
				self.wins (self.p1.name)
			else:
				self.p2.wins += 1
				self.wins (self.p2.name)

		win = self.winner (self.p1, self.p2)

		print ("war is over.{} wins".format (win))

	def winner (self, p1, p2):
		if p1.wins > p2.wins:
			return p1.name
		if p1.wins < p2.wins:
			return p2.name
		return "It was a tie"

game = Game ()
game.play_game ()