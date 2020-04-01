# afficher l'extion d'un fichier saisit au clavier
file = str(input('veuillez saisir le nom du fichier avec l\'extention: '))
f = file.split('.')
print('.{}'.format(f[-1]))