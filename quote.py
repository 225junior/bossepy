# -*-  coding:utf8 -*-
import random

user_choice = input('Entrer Pour Continuer B pour Quitter')

quotes =[  'Alphat, vous ne savez plus lire??',
            'Satané de bordel de putain de Merde!!',
            'Rira bien qui rira le dernier',
            'je taime',
            'dans la jupe de madame',
            'Les français sont très mauvais cinéastres',
            'Mille milliard de mille sabots',
            'tu auras toujour le droit de te faché mais...'
        ]

def getRandom(maListe):
    nbr = random.randint(0,len(quotes) -1)
    item = maListe[nbr]
    return item
while user_choice !='q':
    print (getRandom(quotes))  
