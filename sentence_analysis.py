#! /usr/bin/env python3.6
#coding: utf-8

sentence = """Le sénateur, dont il a été parlé plus haut, était un homme entendu qui 
    avait fait son chemin avec une rectitude inattentive à toutes ces rencontres qui font 
    obstacle et qu'on nomme conscience, foi jurée, justice, devoir; il avait marché droit à 
    son but et sans broncher une seule fois dans la ligne de son avancement et de son intérêt. 
    C'était un ancien procureur, attendri par le succès, pas méchant homme du tout, rendant 
    tous les petits services qu'il pouvait à ses fils, à ses gendres, à ses parents, même à 
    des amis; ayant sagement pris de la vie les bons côtés, les bonnes occasions, les bonnes 
    aubaines. Le reste lui semblait assez bête. Il était spirituel, et juste assez lettré 
    pour se croire un disciple d'Epicure en n'étant peut-être qu'un produit de Pigault-Lebrun.
    [...]
    (Les Misérables, Victor Hugo)
    """

#Toutes les voyelles possibles
#voyelles = "aeiouyAEIOUYéèâàuùû"

#Le compteur de a
count_a = 0

#On parcourt la phrase caractère par caractère
#for letter in sentence:
	#Si le caractère est un "a" ou un "à", on incrémente le compteur
	#if letter == 'a' or letter == 'à':
		#count_a += 1

#Phrase qui donne le nombre de lettres.
#On doit convertir le compteur en chaîne de caractères.
#print("Le texte contient " + str(count_a) + " fois la lettre a")

