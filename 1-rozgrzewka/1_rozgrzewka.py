 #1. Wypisz tekst na konsoli 
 
from os import remove


print("Hello World!")
 

#2. Dodaj dwie liczby i wyświetl na konsoli

a = 5
b = 10

print(a+b)

#3. Przypisz tekst "test" do trzech zmiennych (x,y,z) za pomocą jednej komendy ( w jednej linijce kodu )

x=y=z="test"

#4. Skonwertuj liczbę 6.5 do liczy całkowitej i przypisz do zmiennej d i wypisz

c = 6.5
d=int(c)
print(d)

#5. Wypisz ilość znaków w tekście "Hello World"

e = "Hello World"
print(len(e))

#6. Wypisz pierwszy znak z tekstu "Hello World" - używając zmiennej e

print(e[0])

#7. Usuń spacje z napisu "Hello  World " i wypisz

f = "Hello  World "
fprim = f.replace(" ","")
print(fprim)

#8. Dodaj element "Chevrolet" jako ostatni do listy samochodów 

cars = ["Dodge", "RAM"]
cars.append("Chevrolet")

#9. Usuń element "RAM" z listy samochodów

#cars.remove("RAM")
del cars[1]
print(cars)

#10. Wypisz 2, 3 i 4 element z listy używając zakresu indeksów

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[1:4])

#11. Wypisz wielkość tablicy 'fruits'

print(len(fruits))

#12. Wypisz wszystkie owoce za pomocą pętli 'for'

for x in fruits:
    print(x)

#13. Stwórz funkcję która wypisuje podany w parametrze tekst a następnie ją wywołaj

def funkcja1():
    print("Ta funkcja wywołuje tekst")

funkcja1()
