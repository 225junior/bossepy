# afficher tout les mots d'une string commençant par la lettre a
texte = str(input('veuillez saisir le texte : '))
l = texte.split()
for i in l:
    if i[0] == 'a':
        print(i)