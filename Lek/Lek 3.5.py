'''
Napisz funkcję czy_parzysta(n), która:

    przyjmuje liczbę n,
    zwraca True, jeśli liczba jest parzysta, lub False w przeciwnym razie,
    w programie głównym sprawdź kilka liczb podanych przez użytkownika w pętli.
'''

def czy_parzysta(n):
    if n % 2 == 0:
        print(n, "parzysta")
    else:
        print(n, "nieparzysta")
n=int(input("Podaj liczbę N"))
czy_parzysta(n)
