# ecrire un programme python permetant de compter
# le nombre de voyelles dans une chaine données#
chaine = str(input('veuillez saisir la chaine de caractère : '))
cpt = 0
for i in chaine:
    if i in ('a','e','i','o','y','u'):
        cpt +=1
print('Il y a {} voyelle(s) Dans "{}"'.format(cpt,chaine))