'''
Napisz program, który:

    wczyta od użytkownika 5 ocen (liczb całkowitych) i zapisze je do listy,
    obliczy średnią ocen,
    wypisze komunikat „Zaliczone”, jeśli średnia jest większa lub równa 3.0, w przeciwnym razie „Nie zaliczone”.
'''

listOcen=[]
for i in range(5):
    ocena=int(input("Podaj ocene: "))
    if 1>=ocena or ocena<=6:
        listOcen.append(ocena)
    else:
        print("niema takich ocen")
    i+=1
srednia=sum(listOcen)/len(listOcen)
print("średnią ocena: ", srednia)
if srednia>3.0:
    print("Zaliczone")
else:
    print("Nie zaliczone")
