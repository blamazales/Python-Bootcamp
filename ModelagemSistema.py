# Modelagem Sistema

from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self._renda_mensal = renda_mensal  # Encapsulamento (protegido)

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @abstractmethod
    def tem_cheque_especial(self):
        pass

class Mulher(Pessoa):
    def tem_cheque_especial(self):
        return True

class Homem(Pessoa):
    def tem_cheque_especial(self):
        return False
        
class ContaCorrente:
    def __init__(self, titulares):
        self._titulares = titulares  # Lista de objetos Mulher ou Homem
        self._saldo = 0.0            # Encapsulamento
        self._operacoes = []         # Lista de saques e depósitos

    @property
    def saldo(self):
        return self._saldo

    def _calcular_limite(self):
        # O limite é a soma da renda de todas as mulheres na conta
        limite = 0
        for t in self._titulares:
            if t.tem_cheque_especial():
                limite += t.renda_mensal
        return limite

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._operacoes.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        limite_disponivel = self._saldo + self._calcular_limite()
        
        if valor <= limite_disponivel:
            self._saldo -= valor
            self._operacoes.append(f"Saque: -R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente (incluindo cheque especial).")

    def exibir_extrato(self):
        print(f"\n--- Extrato Banco Delas ---")
        for op in self._operacoes:
            print(op)
        print(f"Saldo atual: R$ {self._saldo:.2f}")
        print(f"Limite de Cheque Especial: R$ {self._calcular_limite():.2f}")

# Criando os clientes
cliente1 = Mulher("Ana Silva", "1199999-8888", 5000.0)
cliente2 = Homem("João Souza", "1197777-6666", 3000.0)

# Criando a conta com ambos como titulares
minha_conta = ContaCorrente([cliente1, cliente2])

# Operações
minha_conta.depositar(1000)
minha_conta.sacar(3000)   # Usa parte do cheque especial da Ana (limite de 5000)
minha_conta.sacar(4000)   # Tenta sacar mais do que o saldo + limite da Ana
minha_conta.exibir_extrato()        