text=input("Podaj dowolny text ").split()
text2=set(text)
print(text2)

unikalni={}
for slowo in text2:
    if slowo.isalpha():
        if slowo in unikalni:
            unikalni[slowo]+=1
        else:
            unikalni[slowo]=1 
print(len(unikalni))
if "Python" in unikalni:
    print("Swietnie, znasz Pythona!")
