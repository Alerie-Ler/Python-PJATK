wyniki = (45, 67, 82, 90, 55, 74, 100, 61)

sr_ocena=sum(wyniki)/len(wyniki)
print("średnia ocena", sr_ocena)

lista=[]
for t in wyniki:
    if t>=sr_ocena:
        lista.append(t)
print("Wyniki powyrze sriednie: ", lista)

wynik=0
for i in wyniki:
    if i>=60:
        wynik+=1
print("Iloscz osob, kto ma > 60: ", wynik)

if 100 in wyniki:
        print("Witam, jestesz najlepszy!")
