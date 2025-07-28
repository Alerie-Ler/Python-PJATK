'''
Napisz program, który przechodzi przez liczby od 1 do 20 i dla każdej liczby:

    wypisuje „parzysta”, jeśli liczba jest parzysta,
    wypisuje „nieparzysta”, jeśli liczba jest nieparzysta.
'''

i=1
while i<=20:
    if i % 2 == 0:
        print(i, "parzysta")
    else:
        print(i, "nieparzysta")
    i += 1
