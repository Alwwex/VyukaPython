# vstupy a b c jsou to stránky trojúhelníku a zjistíme, zda se z nich dá sestrojit trojúhelník

a = float(input("Zadej délku strany a: "))
b = float(input("Zadej délku strany b: "))
c = float(input("Zadej délku strany c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Délka strany nemůže být záporná nebo nulová.")
elif a + b > c and a + c > b and b + c > a:
    print("Lze sestrojit trojúhelník.")
else:
    print("Nelze sestrojit trojúhelník.")