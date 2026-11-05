
vstup = input("Zadej svůj věk: ")


vek = int(vstup)

if vek < 0:
    print("Zadal jsi záporný věk.")
elif vek < 18:
    print("Jsi Dítě.")
    chybi = 18 - vek
    if chybi == 1:
        print("Do dospělosti ti chybí", chybi, "rok.")
    elif chybi <= 4:
        print("Do dospělosti ti chybí", chybi, "roky.")
    else:
        print("Do dospělosti ti chybí", chybi, "let.")
else:
    print("Jsi Dospělý.", vek)



