'''
Napisz program, który:

    zapyta użytkownika, ile kilometrów zamierza przejechać samochodem,
    zapyta o średnie spalanie auta (l/100 km) oraz cenę paliwa za litr,
    obliczy i wyświetli:
        ile paliwa zużyje na trasie,
        ile będzie go to kosztować,
        orientacyjną cenę podróży w przeliczeniu na osobę, jeśli poda liczbę pasażerów.
'''

v=float(input ("Ile kilometrów zamierza przejechać samochodem "))
sp=int(input ("Ile średnie spalanie auta (l/100 km) "))
w=float(input ("Jaka cena paliwa za litr "))
paliwo=v/100*sp
print (paliwo," paliwa zużyl/la na trasie,")
cena=paliwo*w
print (cena," to będzie kosztować,")
pas=int(input ("Ile masz pasażerów? "))
cp=cena/pas
print(cp, " to jest cena dla 1 osoby,")
if v>500:
    print ("Długa trasa – zaplanuj przerwy na odpoczynek!")
