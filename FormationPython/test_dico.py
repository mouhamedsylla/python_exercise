dico = {
    'Janvier' : (31),
    'Février' : (29),
    'Mars' : (31),
    'Avril' : (30),
    'Mai' : (31),
    'Juin' : (30),
    'Juillet' : (31),
    'Aout' : (31),
    'Septembre' : (30),
    'Octobre' : (30),
    'Novembre' : (30),
    'Décembre' : (31)
}

def nbJour_annee(mois, nbJ):
    nbJour = sum(mois[nbJ] for nbJ in mois)
    print("Une année compte "+str(nbJour))

nbJour_annee(dico, 'Janvier')