'''
Napisz program, który:

    wczyta zdanie od użytkownika,
    rozbije je na słowa (split()),
    zbuduje słownik, w którym kluczem jest słowo, a wartością liczba jego wystąpień,
    wypisze wszystkie słowa w kolejności alfabetycznej z ich licznością.


'''
text=input("Podaj dowolny text")
tekst1 = text.split()
print(tekst1)
a={}
for litera in tekst1:
    if litera.isalpha():
        if litera in a:
            a[litera] += 1
        else:
            a[litera]=1
print(a)
