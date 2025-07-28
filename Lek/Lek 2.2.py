'''
Napisz program, który:
    zapyta użytkownika o liczbę N,
    wypisze wszystkie liczby od 1 do N w jednej linii, używając pętli while.
'''

j=1
n=int(input("Podaj liczbę N"))
while j<=n:
    print(j,end=", ")
    j+=1
print()
