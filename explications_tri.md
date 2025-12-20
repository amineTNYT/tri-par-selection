

### Description Détaillée du Tri par Sélection

**Tri par sélection**
Algorithme de tri **instable** et de complexité quadratique O(n²). Son principe est simple : à chaque étape, il sélectionne le plus petit élément restant dans la partie non triée et le place directement à sa position finale.

**Fonctionnement**
L'algorithme opère **en place** avec deux boucles imbriquées. Il divise virtuellement le tableau en deux parties : une partie gauche triée (initialement vide) et une partie droite non triée. À chaque itération, la partie triée s'agrandit d'un élément.

**Tableau initial :**
`t = [8, 77, 1]`

**Étape 1 :**
- Cherche le plus petit élément dans `[8, 77, 1]` → trouve `1` à la position 2
- Échange `8` et `1`
- Résultat : `[1, 77, 8]`

**Étape 2 :**
- Cherche le plus petit élément dans `[77, 8]` → trouve `8` à la position 2
- Échange `77` et `8`
- Résultat : `[1, 8, 77]`

**Tableau trié :**
`t = [1, 8, 77]`


https://github.com/user-attachments/assets/ebd35f58-287f-484c-9544-b39670498db3

**Note Importante sur la Variable `aux` :**

La déclaration de `aux` **dépend du type des éléments dans le tableau `t`**.

Si `t` contient :
- **Entiers** → `aux` doit être `entier`
- **Caractères** → `aux` doit être `caractère`
- **Chaînes de caractères** → `aux` doit être `chaine`
- **Nombres réels** → `aux` doit être `réel`
- **Objets personnalisés** → `aux` doit correspondre au type d'objet

**Exemple :**
```pascal
// Pour un tableau d'entiers
aux: entier(aux=0)

// Pour un tableau de caractères
aux: caractère(aux="")

// Pour un tableau de nombres réels
aux: réel
```



**Toujours déclarer `aux` avec le même type de données que les éléments du tableau** pour éviter les erreurs de type lors des opérations d'échange.
<img width="1691" height="825" alt="Capture d’écran 2025-11-04 193836" src="https://github.com/user-attachments/assets/e8897224-c346-4875-972d-8f2138182e4c" />
<img width="1651" height="762" alt="Capture d’écran 2025-11-04 193906" src="https://github.com/user-attachments/assets/99d4cf07-18f0-41ac-9fe1-99aae921f849" />
<img width="1110" height="636" alt="Capture d’écran 2025-11-04 193925" src="https://github.com/user-attachments/assets/89ce2958-6bdd-474f-a7f3-eedbaae72913" />
### 🎥 Vidéo Démo : Tri par Sélection Animé (Explication Pas à Pas)

[![Tri par Sélection Animé - Cliquez pour regarder](https://img.youtube.com/vi/r7g38PYUIAU/maxresdefault.jpg)](https://www.youtube.com/watch?v=r7g38PYUIAU)

*Cliquez sur l'image pour lancer la vidéo sur YouTube (animation interactive, code Python & pseudocode expliqués !)*
