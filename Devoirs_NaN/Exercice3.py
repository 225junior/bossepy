# Ecrire une saisie filtrée d'un entier dans l'intervalle fermé 1 à 10 Afficher la saisie

#debut
nbr = int(input('Saisissez un chiffre compris entre 1 et 10 : '))
while nbr<0 or nbr>10:
    print('Erreur! Saisissez un chiffre compris entre 1 et 10 ')
    nbr = int(input())
print(nbr)
#fin230