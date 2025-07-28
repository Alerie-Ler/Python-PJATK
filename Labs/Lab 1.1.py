'''
Napisz program, który:

    wczyta temperaturę w stopniach Celsjusza,
    przeliczy ją na stopnie Fahrenheita, używając wzoru:
    [ F = C * 9/5 + 32 ],
    wyświetli wynik w formie:
    „25°C to 77°F”.
'''

c=int(input ("Jaka jest temperatura w stopniach Celsjusza "))
F=c*9/5+32
print (c, '°C to jest', F, '°F')


