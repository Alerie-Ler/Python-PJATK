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
    return wynik

a=int(input("a="))
b=int(input("b-"))
wynik = funkcję_prostokat(a, b)
print(wynik)
