'''
Napisz program, który:

    losuje liczbę od 1 do 10,
    prosi użytkownika o zgadywanie liczby, aż zgadnie,
    wyświetla komunikat: „Za mało” lub „Za dużo”, a po trafieniu: „Brawo!”.
'''
import random
i=random.randint(1,10)
n=0
while i!=n:
    n=int(input("Zgadaj liczbe"))
    if i<n:
        print("Za dużo ")
        continue
    elif i>n:
        print("Za mało")
        continue
    else:
        print("Brawo!")
