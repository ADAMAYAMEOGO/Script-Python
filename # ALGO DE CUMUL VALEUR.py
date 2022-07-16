# ALGO DE CUMUL VALEUR

# 1ERE FACON DE FAIRE
""" def cumul_valeur(liste):
    if liste==[]: Cette partie n'est pas obligatoire car si la liste est vide, la boucle n'aurait pas lieu.
        print(liste)
    resultat=[]
    for i in range(len(liste)):
        somme=sum(liste[0:i+1])
        resultat.append(somme)
    return resultat
list_valeur=[1,2,3,4,5,6]
print(f"Le cumul des valeur de la liste {list_valeur} est {cumul_valeur(list_valeur)}") """
#2EME FACON DE FAIRE
""" def cumul_valeur(liste):
    return [sum(liste[0:i+1]) for i in range(len(liste))]


list_valeur=[1,2,3,4,5,6]
print(f"Le cumul des valeur de la liste {list_valeur} est {cumul_valeur(list_valeur)}")
 """
#3EME POSSIBILITE
def cumul_valeur(liste):
    if not liste:
        return []
    resultat=[liste.pop(0)] 
    #==== la methode pop recupère le premier element de la liste et le retirer en même temps.
    for i in liste:
        resultat.append(i+resultat[-1])
    return resultat

list_valeur=[1,2,3,4,5,6]
print(f"Le cumul des valeur de la liste {list_valeur} est {cumul_valeur(list_valeur)}")

