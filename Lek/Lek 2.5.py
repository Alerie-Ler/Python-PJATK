'''
Napisz program, który wypisze kwadraty wszystkich liczb od 1 do 10 w formie:

1^2 = 1
2^2 = 4
3^2 = 9
'''

for k in range(1,11):
    for j in range(1,11):
        print(k, "^", j, "=", k**j)
