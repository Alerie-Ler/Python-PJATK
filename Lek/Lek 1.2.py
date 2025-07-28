'''
W ZOO w Gdańsku bilet normalny kosztuje 45 zł, a ulgowy 35 zł.

    Dzieci poniżej 3 roku życia oraz seniorzy powyżej 70 lat wchodzą za darmo
    Dzieci i młodzież do 26 lat korzysta z biletów ulogwych
    powyżej 26 roku życia obowiązuje bilet normalny Napisz program, który przyjmie od użytkownika liczbę - wiek osoby i w odpowiedzi wydrukuje kwotę, którą ta osoba powinna zapłacić za wstęp.

'''

n=45
u=35
wiek=int(input("Ile masz lat?"))
if wiek<3 or wiek>70:
    print ("Bilet jest za darmo",0)
elif wiek>3 and wiek<26:
  print("Bilet ulgowy",u)
else:
  print("Bilet normalny",n)
