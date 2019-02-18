"""
Cour Python - Notebook 1
"""

"""Doc
ligne 1
ligne 2
ligne 3"""

#doc sur une ligne


########################


#Assignation de variables
a = b = c = 1

#Affiche sur la console le contenu du print
print(a)
print(b)
print(c)

########################

#Assignation de variables
chaine = "hello world"
nombre = 12345
counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string print counter

#Affichage du contenu des variables
print(miles)
print(counter)
print(name)

########################

#Travail sur les listes
list = [ 'abcd', 123 , 1.23, 'efgh', 45.6 ]
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element


########################

#Fonctions de conversion de variables
"""
int() , long(),float(),complex()
str(), chr()
Eval() --> to object
tuple(), list(), set()
dict()
Unichr(),ord(),hex(),oct()
+,-,*,/
%,**,// (mod / puissance et division)
"""

chaine = "123"
nombre = int(chaine)    #chaine vers numérique

chaine = str(456)   #numérique vers chaine
print(chaine)

print(str(458 % 4)) #modulo


########################

#Importations de librairies
import sys
import math

print(str(math.cos(math.pi)))


#Pour attendre une entrée utilisateur
#input()


########################

#dictionary
dict = {'Name': 'James Gordon', 'Age': 36, 'Class': 'Inspecteur'}
print("dict['Name']:" , dict['Name'])
print("dict['Age']:" , dict['Age'])


########################

#lecture de fichier

contenu = open("toto.txt")
for line in contenu:
    print(line)
    if line.startswith('hola'):
        print("hé ombre !")
print("End of file")

########################

# conditions if
totoIf = 50
if(totoIf == 50): print ("totoIf")

########################

#Iteration sur des lettres
mot = 'Python'
for letter in mot:
    print(letter)
    
########################

# déclaration de fonction
def PrintTest(mot):
   print(mot)

#appel de la fonction
PrintTest(mot)

########################

#imports et utilisation de module
import module1
module1.PrintTest("Ed Nygma")


########################
#affichage du contenu du module

for mod in dir(math):
    print(mod)

########################
########################
########################
########################
########################
########################


