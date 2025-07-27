'''
Napisz funkcję prostokat(a, b), która:

obliczy pole prostokąta (a*b),
obliczy obwód (2*(a+b)),
zwróci wynik jako słownik:
{"pole": ..., "obwod": ...}
'''
def funkcję_prostokat(a, b):
    pole = a * b 
    obwod = 2 * (a + b)
    wynik = {
        "pole": pole,
        "obwod": obwod
    }
    return wynik.items()

print (funkcję_prostokat(4,8))
