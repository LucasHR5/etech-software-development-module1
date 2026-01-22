class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo # Atributo privado

    def depositar(self, quantia):
        self.__saldo += quantia

    def sacar(self, quantia):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
            return True
        else:
            return False
        
    def get_saldo(self):
        return self.__saldo
    
    def set_titular(self, novo_titular):
        self.titular = novo_titular