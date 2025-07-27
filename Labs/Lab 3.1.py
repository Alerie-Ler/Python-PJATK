'''
Napisz funkcję licz_litery(tekst), która:

przyjmie string,
zwróci słownik z liczbą wystąpień każdej litery (ignorując wielkość liter i znaki interpunkcyjne),
wypisze wynik w formie:
a: 3
b: 1
'''

tekst = input("Podaj tekst: ")

def licz_litery(tekst):
    tekst = tekst.lower()
    iloscz = {}
    for litera in tekst:
        if litera>="a" and litera<="z":
            if litera in iloscz:
                iloscz[litera]+=1
            else:
                iloscz[litera]=1
    return iloscz
    
wynik = licz_litery(tekst)
for key, value in sorted(wynik.items()):
    print(f"{key}: {value}")
