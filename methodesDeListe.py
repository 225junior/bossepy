# -*- coding:utf8 -*-
quotes =[  'Alphat, vous ne savez plus lire??',
            'Satané de bordel de putain de Merde!!',
            'Rira bien qui rira le dernier',
            'je taime',
            'dans la jupe de madame',
            'Les français sont très mauvais cinéastres',
            'Mille milliard de mille sabots',
            'tu auras toujour le droit de te faché mais...'
        ]
print (quotes.index('Rira bien qui rira le dernier'))#retourne l'index dans la liste
print (type(quotes))#le type de variable
print (len(quotes))#nombre d'éléments dans la liste quotes
print (quotes[-1])#accede au dernier élément de la liste
quotes.pop(1)#supprime l'élément déindex 1: le deuxieme élément
quotes.insert(0,'Je viens tous vous surclasser')
print (quotes)
fdjfd