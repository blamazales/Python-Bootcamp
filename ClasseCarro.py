# Implementação da Classe Carro

class Carro:
    # Passo 2: Atributos (Método Especial __init__)
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    # Passo 3: Comportamentos (Métodos)
    def liga(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} ligou.")
        else:
            print(f"O {self.modelo} já está ligado.")

    def desliga(self):
        if self.ligado:
            if self.velocidade == 0:
                self.ligado = False
                print(f"O {self.modelo} desligou.")
            else:
                print("Não é seguro desligar o carro em movimento!")
        else:
            print(f"O {self.modelo} já está desligado.")

    def acelera(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"Acelerando... Velocidade atual: {self.velocidade} km/h.")
        else:
            print("Não é possível acelerar com o carro desligado.")

    def desacelera(self, decremento):
        if self.velocidade > 0:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"Desacelerando... Velocidade atual: {self.velocidade} km/h.")
        else:
            print("O carro já está parado.")