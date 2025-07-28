'''
Napisz program, który:

    poprosi użytkownika o rok urodzenia,
    na podstawie obecnego roku (np. 2025) obliczy wiek,
    wyświetli komunikat:
    „Jesteś pełnoletni” lub „Jesteś niepełnoletni” (próg 18 lat).
'''

r=2025
wiek=int(input("Jaki twoj rok urodzenia?"))
if wiek<=2007:
    print ("Jesteś pełnoletni")
else:
	print("Jesteś niepełnoletni")
