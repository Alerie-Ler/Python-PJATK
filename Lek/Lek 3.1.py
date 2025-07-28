'''
Zadanie bez mądrego celu. Napisz swój słownik zawierający co najmniej 7 kluczy, a następnie wypróbuj wszystkie metody z listy powyżej
'''
kot={
    "imie":"Dizi",
    "rasa": "zwykla",
    "rok_urodzenia": 2013,
    "kolor skury": "czarny",
    "kolor oczek": "zolty",
    "waga": 6.5,
    "pol": "male"
}
print(kot)
x = kot.keys()
print(x)
z=kot.items()
print(z)
c=kot.pop('imie', None)
print(c)
kopia = kot.copy()
print(kopia)
n=kot.popitem()
print(n)
dict.fromkeys(['a', 'b'], 0)
