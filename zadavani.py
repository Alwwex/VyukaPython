vstup1 = input("Zadej číslo: ")
vstup2 = input("Zadejte číslo: ")

cislo1 = float(vstup1)
cislo2 = float(vstup2)
vysledek = cislo1 + cislo2

print("Součet čísel je:",vysledek,".")
print("Součet čísel je:" + str(vysledek) + ".")

print("Součet čísel je: {}.".format(vysledek))
print(f"Součet čísel je: {vysledek}.")

print("Součet čísel je: %s." % vysledek)