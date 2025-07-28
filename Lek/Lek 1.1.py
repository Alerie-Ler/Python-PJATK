'''
Twoje zadanie:

    Zapytaj użytkownika o wiek,
    zapytaj, czy jest studentem do 26 roku życia (tak/nie),
    zapytaj o dzień tygodnia (np. „poniedziałek”),
    wyświetl kwotę do zapłaty po uwzględnieniu ewentualnej zniżki.
'''

n=30
st=20
sen=15
wiek=int(input("Ile masz lat?"))
status=bool(input("Czy jestesz studentem?"))
dzien=string(input("Jaki to dzien tygodnia?"))
student=false
if status=="tak":
    student = true
    elif status=="nie":
    student = false
if wiek<=4:
    print ("Bilet jest za darmo",0)
elif wiek >= 65:
    print("Bilet ulgowy", sen)
elif wiek<26 and student:
    print("Bilet ulgowy", st)
else:
	print("Bilet normalny",n)

if dzien=="sroda":
    if wiek <= 4:
        print("Bilet jest za darmo", 0)
    elif wiek >= 65:
        print("Bilet ulgowy", sen-5)
    elif wiek < 26 and student:
        print("Bilet ulgowy", st-5)
    else:
        print("Bilet normalny", n-5)
