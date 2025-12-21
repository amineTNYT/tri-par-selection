from numpy import array

# Fonction pour saisir et valider la taille du tableau
def saisir():
    n = int(input("Donner le taille du tableau=:"))
    while not (3 <= n <= 5):
        n = int(input("Donner taille du tableau=:"))
    return n

# Fonction pour remplir le tableau avec les saisies de l'utilisateur
def remplir(t, n):
    for i in range(0, n):
        t[i] = int(input("t[" + str(i) + "]=:"))


# procédure de tri utilisant l'algorithme de tri par sélection
def tri(t,n):
    for i in range(n):
        for j in range(i+1,n):
            if t[i]>t[j]:
                aux=t[j]
                t[j]=t[i]
                t[i]=aux

# Fonction pour afficher le tableau
def afficher(t, n):
    # Afficher chaque élément du tableau séparé par "|"
    for i in range(0, n):
        print(t[i], end="|")

# Programme Principal
n = saisir()  # Saisir la taille du tableau
t = array([int()]*n)  # Créer un tableau numpy de taille n
remplir(t, n)  # Remplir le tableau avec les valeurs

# Afficher le tableau avant le tri
print("le tableau avant le tri")
afficher(t, n)
print()

# Trier le tableau
tri_seléction(t, n)

# Afficher le tableau après le tri
print("le tableau aprés le tri")
afficher(t, n)


