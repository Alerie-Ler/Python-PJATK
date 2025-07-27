'''
Napisz funkcję formatuj(tekst), która:

usunie nadmiarowe spacje z początku i końca tekstu,
zamieni wszystkie litery na małe,
zamieni w tekście słowo “python” na “PYTHON”.
'''

tekst = input("Podaj text: ")

def formatuj(tekst):
    tekst=tekst.strip().lower().replace("python","PYTHON")
    print(tekst)

formatuj(tekst)
