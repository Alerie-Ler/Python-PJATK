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

dlugie = {chujnia for chujnia in unikalne if len(chujnia) > 5}
print(", ".join(dlugie))

if "Python" in unikalne:
    print("Uczestnicy lubią Pythona!")
