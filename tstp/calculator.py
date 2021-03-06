#calculette

a = input ("Choisis un nombre:")
a = int (a)

def calculette (b):
	return a + 2
print (calculette(a))



a = input ("choisis un autre nombre:")
a = int (a)

def calculette2 (b):
	return a - 5
print (calculette2(a))


a = input ("Choisis un nombre:")
c = int(a)
d = input ("choisis un autre nombre:")
e = int (d)

choix_du_test = input ("Addition ou Soustraction ?")
reponse_test = int (choix_du_test)

def calculettetest (b):
	if reponse_test == "Addition":
		return c + e
	if reponse_test == "Soustraction":
		return c - e
	
result = calculettetest (b)
print (result)