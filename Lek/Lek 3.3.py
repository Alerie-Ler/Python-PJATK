'''
Napisz program, który:

    wczyta od użytkownika dowolny tekst,
    usunie z niego spacje i znaki interpunkcyjne,
    policzy, ile razy występuje każda litera (bez rozróżniania wielkości liter),
    wypisze wynik w formie:

    a: 3
    b: 1
    c: 5

'''
texst=input("Podaj dowolny takst")
print(texst.strip().strip(" ,.:;"))

licznik = {}
for litera in texst:
    if litera.isalpha():
        if litera in licznik:
            licznik[litera]+=1
        else:
            licznik[litera]=1
print(licznik)
