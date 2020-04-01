# Ecrire un programme qui renvoie le premier mot d'un texte
texte = str(input('veuillez saisir le texte : '))
l = len(texte)
for i in range(0,l):
    if texte[i]==' ':
        f = texte[:i]
        break
print(f)

# le prof

# i = 0
# pre=''
# while texte[i] != ' ':
#     pre = pre + texte[i]
#     i+=1
# print(pre)