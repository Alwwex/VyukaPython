cislo = input("Zadejte číslo: ")
cislo = int(cislo)

sude = cislo % 2 == 0
liche = cislo % 2 != 0

if sude:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")