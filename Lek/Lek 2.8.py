import random

lista=[]
for _ in range(10):
    i=random.randint(0,100)
    lista.append(i)
wyniki=tuple(lista)
print(lista)

liczba=[apple for apple in wyniki if apple >= 50]
print("Liczba ocen powyżej 50: ", liczba)
max=max(wyniki)
min=min(wyniki)
print("maksymalne: ", max)
print("minimalne: ", min)
