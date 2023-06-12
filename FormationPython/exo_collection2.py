"""chauffeur = ["Mouhamed", "Moussa", "Issa", "Modou"]
distance_chauffeur_km = [1.0, 0.2, 0.01, 0.1]

val = distance_chauffeur_km[0]
index = -1
for i in distance_chauffeur_km:
    index += 1
    if i < val:
        val = i
        index_chauffeur = index

print("la distance minimale : "+str(val)+" km")
print("Nom chauffeur : "+chauffeur[index_chauffeur])"""

chauffeur_et_km = [("mouhamed", 1.0), ("Moussa", 0.2), ("Issa", 10), ("Modou", 0.1)]

"""val = chauffeur_et_km[0][1]
for i in range(0, len(chauffeur_et_km)):

    if chauffeur_et_km[i][1] < val:
        val = chauffeur_et_km[i][1]
        val1 = i

print("Nom chauffeur :", chauffeur_et_km[val1][0], "    Nombre de km :", val)"""

val = chauffeur_et_km[0]
for i in chauffeur_et_km:
    if i[1] < val[1]:
        val = i

print("Nom chauffeur :", val[0], "Distance :", val[1])





