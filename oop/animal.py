class Animal:
    #constructor
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f'El este {self.nume} si are {self.varsta} ani.'

    def __unicode__(self):
        return f'El este {self.nume} si are {self.varsta} ani.'

    def __repr__(self):
        return f'El este {self.nume} si are {self.varsta} ani.'

    def sunet(self):
        pass


class Pisic(Animal):
    def poo_how(self):
        return 'Face la litiera sa adune sclavii.'
    def sunet(self):
        return 'Miorlau'


class Cățăl(Animal):
    def poo_how(self):
        return 'Fac pe Dristorului sa calcam noi in el.'
    def sunet(self):
        return 'Ham un baietel'


class Hipopotam(Animal):
    def poo_how(self):
        return 'Imprastiat.'
    def sunet(self):
        return 'grunt grunt!'

party_animals = []
rasa = input('Introdu rasa animalului(catel, pisic, hipopotam)= ')
while rasa:
    nume = input('Boteaza-l cumva ')
    varsta = input('Introdu o varsta ')
    ce_animal = None
    if rasa == 'catel':
        ce_animal = Cățăl(nume, varsta)
    elif rasa == 'pisic':
        ce_animal = Pisic(nume, varsta)
    elif rasa == 'hipopotam':
        ce_animal = Hipopotam(nume, varsta)

    party_animals.append(ce_animal)
    rasa = input('Introdu rasa animalului( catel, pisic, hipopotam)= ')

party_animals.append(Cățăl('Buddy', 5))
party_animals.append(Pisic('Petrica', 1.5))
party_animals.append(Hipopotam('John', 10))
for animal in party_animals:
    print(f'{animal.nume} face sunetul {animal.sunet()} si face caca asa: {animal.poo_how()}')