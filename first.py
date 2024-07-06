#1
nom = input("Entrez votre nom : ")
age = input("Entrez votre âge : ")

print(f"Votre nom est {nom} et vous avez {age} ans.")

#2
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somme = sum(nombres)
print(somme)  # Affiche 55

#3
nombre = int(input("Entrez un nombre entre 0 et 10 : "))
if nombre % 2 == 0:
    result = "pair"
else:
    result = "impair"
print(f"Votre nombre est {result}.")
