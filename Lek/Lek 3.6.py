'''
Napisz funkcję najwieksza(a, b, c), która:

    przyjmuje trzy liczby,
    zwraca największą z nich,
    w programie głównym wczytaj trzy liczby od użytkownika i wypisz wynik.

'''

def najwieksza(a, b, c):
    list = [a, b, c]
    for i in range(3):
        list.append(n)
    k=max(list)
    print(f"Najwienksa {k}")

a = int(input("Podaj numer 1: "))
b = int(input("Podaj numer 2: "))
c = int(input("Podaj numer 3: "))
najwieksza(a, b, c)
