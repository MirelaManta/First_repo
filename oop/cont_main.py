from oop.cont_bancar import ContBancar
from oop.dog import Dog
from oop.dog import JackRussellTerrier, Buldog, TolomacBreed

cont1 = ContBancar('Mirela M', 'R01126536')
cont2 = ContBancar('Tibi O', 'R0276357')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300)
cont2.plataCard(100)
cont2.plataCard(200)

cont1.interogareSold()
cont2.interogareSold()


# catel1 = Dog('Buddy', 4, 'Jack Russell Terrier')
# catel2 = Dog('Betty', 1, 'Bulldog')
# catel3 = Dog('Max', 2, 'Tolomac Breed')
# catel4 = Dog('Ursu', 5, 'Tolomac Breed')

doggo1 = JackRussellTerrier('Buddy', 4)
doggo2 = Buldog('Betty', 2)
doggo3 = TolomacBreed('Max', 1)
doggo4 = TolomacBreed('Ursu', 5)

print(doggo3.speak('awoof'))
print(doggo1.speak())
print(doggo4.description())
print(doggo2.species)
print(type(doggo1)) # too see which class is part of
print(isinstance(doggo2, Dog))  # checks if dogo2 is an instance of the Dog class



#
# print(catel3.speak('Yap'))
# print(catel1.speak('bark! bark!'))
# print(catel2.description())



# tema
# clasa Angajat
# nume, prenume, salariu, vechime, functie
# constructor: nume, prenume, salariu, functie, vechime
# metode: descriere
# marire salariu in f de vechime
# daca are vechime sub 5 ani,marim cu 300 lei, peste 5 ani, 500 lei
# actualizare vechime(param noua vechime)
    # self.vechime = noua_vechime
# descriere
