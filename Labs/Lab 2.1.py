produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "banan", "kiwi", "mango", "pomidor", "herbata", "kawa")
print(f"W sklepie sa nastempni produkty {produkty}")
koszyk = []
for i in range (3):
    while True:
        produkt=str(input("Dodaj produkt").strip().lower())
        if produkt in produkty:
            koszyk.append(produkt)
            break
        else:
            print ("Niema takiego w sklepie")
print("Zakupy: ")   
for koszyk in sorted(koszyk):
    print(koszyk)
