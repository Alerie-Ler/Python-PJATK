lista = []
for _ in range(3):
    kom = input("Dodaj komentarz").strip()
    lista.append(kom)
print(lista)

unikalne = set()

for komentarz in lista:
    slowo = komentarz.split()
    unikalne.update(slowo)
    
print(", ".join(unikalne))
print(f"Ilisc unikalny {len(unikalne)}")

dlugie = {k for k in unikalne if len(k) > 5}
print("Ilosc unikalnych, które mają więcej niż 5 liter: ", ", ".join(dlugie))

if "Python" in unikalne:
    print("Uczestnicy lubią Pythona!")
