#Ex1     TD/TP3
"""name = "SPATIPHYLLUM"
name0 ="spatiphyllum"
name1= input("Entrer le mot correspandant :")
if name1== name:
    print("Yes -spathiphyllm is the best plant ever ")
elif name0 ==name1:
    print ("No, I want a big Spatiphyllum")
else:
    print ("spatiphyllum ! Not", name1)
    """




#EX2
"""
number = int(input("Entrer un nombre  a:"))
number1 =int(input("Entrer un autre nombre  b: "))
if number1 != 0:
    result = number // number1
    print("Le resultat de la division a/b est :", result)
else:
    print ("Erreur: Division par zero impossible")

    """



#EX3
"""
nombre = int(input("Entrer un nombre entiere:"))
print ("la valeur absolue de", nombre, "est", -nombre)
"""




#EX4
"""
a=int (input("Entrer un nombre a:"))
b= int (input ("Entrer un nombre b :" ))
 
if a-b >0:
    print("Resultat positif ")
elif a-b ==0 : 
    print("Resultat nul ")
else:
    print("Resultat negatif ")

"""



#EX5

"""
alphabet = input("Entrer une lettre de l'alphabet :")
if alphabet in "aeuyioAEUYIO":
    print ("la lettre est une voyelle ")
else: 
    print ("la lettre est une consonne")
"""



#EX6

"""
revenu = float(input("Entrer votre revenu :"))
if revenu <= 85528:
    impot = round(0.18 * revenu - 556.2)
elif revenu > 85528:
    impot = round(14839.2 +0.32 *( revenu -85528))

if impot < 0:
    impot = 0

print("The tax is :", impot, "thalers")
"""





#EX8
"""
annee= int (input("Entrer une annee:"))

if annee<1582:
    print ("hors de la periode du calendrier grégorien")
elif annee % 4 !=0  :
    print (f"{annee} est commune")
elif annee %100 !=0:
    print (f"{annee} est bissextile")
elif annee % 400 !=0:
    print (f"{annee} est commune")
else:
    print(f"{annee} est bissextile")

"""




#EX1      TD4
"""

print ("La table de multiplication  de 3 : ")

for i in range (1,11,1):
    result= i*3
    print(f"{i}*3 = ",result )


nombre = int (input("Entrer un nombre pour afficher sa table de multiplication :"))
for i in range (1,11,1):
    result= i*nombre
    print(f"{i}*{nombre} = ",result )


"""




#EX2
"""
nombre = int(input("Entrer un nombre entier positif :"))
somme = 0
impairs = []

for i in range(1, nombre + 1, 2):
    somme += i
    impairs.append(str(i))

chaine = " + ".join(impairs)

print(f"La somme des entiers impairs de 1 à {nombre} est : {chaine} = {somme}")


"""



#EX3
"""
nombre =int(input("Entrer un nombre entier :"))
for i in range (nombre,0,-1):
    print (i)
"""




#EX5
"""
nombre =int (input("Donner un nombre : "))
print(f"le nombre de chiffres est {len(str(nombre))}")
"""


#EX4
"""
argent = float(input("Entrer le somme d'argent :"))
while argent >0:
  print("Entrer les info de produit :")
  nom= str(input("le nom:"))
  price= float(input("le prix:")) 
  if argent - price >=0:
      argent -= price
      print(f"Vous avez acheté {nom} pour {price} thalers. Il vous reste {argent} thalers.")
  else :
      newprice = price - argent
      print (f"Il vous manque {newprice} thalers pour acheter {nom}.")
      break
    



"""


#EX6

"""
total_blocks = int(input("Entrer le nombre de blocs: "))
somme = 0
height = 0

for i in range(1, total_blocks + 1):
    somme += i
    if somme > total_blocks:
        break
    height = i

print("La hauteur maximale de la pyramide est :", height)
"""

