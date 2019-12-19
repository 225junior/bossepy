print("Ce Programme Afiche à l'ecran le type de l'année que vous avez allez saisir au clavier: Bisextile ou Non bisextile")
print('')
annee = int(input("Veuillez saisir l'année (Ex:2012) : "))
all = annee % 400 
centieme = annee % 100
fortime = annee % 4
if all == 0:
    print("L'année ",annee," Est Bisextile")
elif centieme == 0 :
    print(annee, " N'est pas une Année Bisextile")
elif fortime == 0:
    print("L'année ",annee," Est Bisextile")
else:
    print(annee, " N'est pas une Année Bisextile")