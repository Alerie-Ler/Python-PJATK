'''
Stwórz słownik opisujący studenta (imie, nazwisko, rok, kierunek, oceny jako lista).
Następnie:

dodaj nowy klucz średnia i oblicz średnią ocen,
wypisz wszystkie klucze i wartości w czytelnej formie.
'''

student = {
    "imie": "Daria",
    "nazwisko": "Nastenko",
    "rok": "2025",
    "kierunek": "IT",
    "oceny": {
        "matematyka": 4,
        "grafika": 6,
        "programowanie": 5,
        "fizyka": 4,
    }
}
wse_oceny = student["oceny"].values()
sr_ocena = sum(wse_oceny)/len(wse_oceny)
student["srednia"]=sr_ocena
print("Wszystkie klucze: ",student.keys())
print("\nWszystkie wartości: ",student.values())
