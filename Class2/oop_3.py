from abc import ABC, abstractmethod

class Funcionario(ABC):

    #abcstract base class 
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.__salario_base = salario_base  # Atributo privado

    @property 
    def salario(self):
        return self.__salario_base
    
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario >= 0:
            self.__salario_base = novo_salario
        else:
            raise ValueError("O salário não pode ser negativo.")

    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
  def calcular_bonus(self):
      return self.salario * 0.20
    
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

timeTi = [
    Gerente("Ana", 8000),
    Desenvolvedor("Bruno", 5000),
    Desenvolvedor("Carla", 6000)
    ]

print("folha de pagamento:")
for funcionario in timeTi:
    print(f"{funcionario.nome}: Salário: R${funcionario.salario}, Bônus: R${funcionario.calcular_bonus()}")

timeTi[1].salario = 5500  # Atualizando o salário do Bruno
print(f"Salário atualizado de {timeTi[1].nome}: R${timeTi[1].salario}")