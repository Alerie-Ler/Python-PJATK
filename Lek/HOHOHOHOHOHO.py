def obliczenie():
    lista = wwod()
    if lista is None: # Added a check in case wwod() returns None due to invalid input
        return

    x = lista[1]
    wynik = None # Initialize wynik to None

    if x == '+':
        wynik = dodaj(lista[0], lista[2])
    elif x == '*':
        wynik = pomnoz(lista[0], lista[2])
    elif x == '-':
        wynik = odejmij(lista[0], lista[2])
    elif x == '/':
        wynik = podziel(lista[0], lista[2])
    elif x == '^':
        wynik = potega(lista[0], lista[2])
    else:
        print("Blad: Nieznany operator.") # More descriptive error message

    if wynik is not None: # Only print if a valid result was obtained
        print("Wynik: ", wynik)
    return wynik
