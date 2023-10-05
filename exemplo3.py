#usando como exemplo um código de animal, aqui o objeto "falar" recebe diferentes comportamentos em situações variadas
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Pato(Animal):
    def falar(self):
        return "Quack!"

def fazer_barulho(animal):
    return animal.falar()

cachorro = Cachorro()
gato = Gato()
pato = Pato()

print(fazer_barulho(cachorro))
print(fazer_barulho(gato))    
print(fazer_barulho(pato)) 
