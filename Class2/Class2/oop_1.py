class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligarMotor(self):
        print(f"Ligando motor de: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")
    
    def desligarMotor(self):
        print(f"Desligando motor de: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")
    
    
meuCarro = Carro("Toyota", "Corolla", 2020, "Prata")

meuCarro.ligarMotor()

carroDoAmigo = Carro("Honda", "Civic", 2019, "Preto")
carroDoAmigo.ligarMotor()

class moto(Carro):
    def __init__(self, marca, modelo, ano, cor, tipo):
        super().__init__(marca, modelo, ano, cor)
        self.tipo = tipo

    def empinar(self):
        print(f"A moto {self.marca} {self.modelo} está empinando!")