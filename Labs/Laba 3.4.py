'''
Napisz funkcję odwroc_slowa(zdanie), która:

rozbije zdanie na słowa (split),
odwróci każde słowo osobno (np. "Ala ma kota" → "alA am atok"),
połączy słowa w nowy string i zwróci wynik.
'''

def odwroc_slowa(zdanie):
    wynik = list(zdanie)
    left, right = 0, len(wynik)-1

    while left < right:
        wynik[left], wynik[right] = wynik[right], wynik[left]
        left += 1
        right -= 1 
    return ''.join(wynik)

zdanie = input("Text: ")
n = odwroc_slowa(zdanie)
print(n)
