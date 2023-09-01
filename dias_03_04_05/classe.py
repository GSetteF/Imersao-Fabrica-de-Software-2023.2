#classe abstrata
from abc import ABC, abstractmethod

class IAnimal(ABC): #criar_classe


    @abstractmethod #syntax_sugar
    def falar(self): #criar_metodo
        """defina na classe filha"""

    @abstractmethod
    def andar(self):
        """defina na classe filha"""

class Cachorro(IAnimal): #Cachorro herda de IAnimal, pode herdar mais classes
    def falar(self):
        print("AuAu")

    def andar(self):
        print("Ando com 4 patas")

class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome  #protegido (somente nela + filhas)
        self.idade = idade #publica (qualquer lugar)
        self.__humano = True #privado (só nessa classe)

    def falar_pessoa(self):
        print("Falando")
    
    def mostra_nome(self):
        print(f"Nome é: {self._nome}")

#animal = IAnimal()

pingo = Cachorro()
pingo.andar()
pingo.falar()

humano = Pessoa("Gabriel", 20)
humano.falar_pessoa()
humano.mostra_nome()
