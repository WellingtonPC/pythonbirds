"""
Criar uma classe Carro com os seguites atributos, esses atributos serão outras classes:
    1 - Motor
    2 - Direção

O Motor terá a responsabilidade de controlar a velocidade.
Composição:
    1 - Atributo de dado velocidade
    2 - Método acelerar, que deverar incrementar a velocidade em uma unidade
    3 - Método frear, que deverá diminuir a velocidade em duas unidades

A Direção terá a responsabilidade de controlar o direcionamento do Carro.
Composição:
    1 - Atributo valor da direção. Valores possíveis: Norte, Sul, Leste, Oeste. Valor padrão: Norte
    2 - Método virar a direita
    3 - Método virar a esquerda 
    Obs. Norte (Cima), Sul (Baixo), Leste(Esquerda), Oeste(Direita)


"""


#Estudo de composição


class Carro:

    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor
    

    def calcular_velocidade(self):
        return self.motor.velocidade


    def acelerar(self):
        return self.motor.acelerar()


    def frear(self):
        return self.motor.frear()


    def sentido(self):
        return self.direcao.sentido


    def virar_a_direita(self):
        return self.direcao.virar_a_direita()


    def virar_a_esquerda(self):
        return self.direcao.virar_a_esquerda()


class Motor:

    def __init__(self):
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 1
        return f'Acelerando. Velocidade: {self.velocidade}'


    def frear(self):
        self.velocidade -= 2

        if self.velocidade < 0:
            self.velocidade = 0

        return f'Freando. Velocidade atual: {self.velocidade}'


class Direcao:

    direcoes_possiveis = ('Norte', 'Leste', 'Sul', 'Oeste')

    def __init__(self, sentido='Norte'):
        self.sentido = sentido


    def virar_a_direita(self):
        indice = self.direcoes_possiveis.index(self.sentido) 
        if indice == len(self.direcoes_possiveis)-1:
            self.sentido = self.direcoes_possiveis[0]
            
        else:
            self.sentido = self.direcoes_possiveis[indice + 1]
           

    def virar_a_esquerda(self):
        indice = self.direcoes_possiveis.index(self.sentido) 
        if indice == 0:
            self.sentido = self.direcoes_possiveis[-1]
        else:
            self.sentido = self.direcoes_possiveis[indice - 1]


if __name__ == '__main__':

    #Teste classe Direção
    m = Motor()
    print(m.acelerar())
    print(m.acelerar())
    print(m.acelerar())
    print(m.frear())
    print(m.frear())
    print(m.frear())


    #Teste classe Direção
    
    d = Direcao()

    print(d.direcoes_possiveis, d.sentido)
    for item in range(5):
        d.virar_a_direita()
        print(d.direcoes_possiveis, 'Direita ', d.sentido)

    for item in range(5):
        d.virar_a_esquerda()
        print(d.direcoes_possiveis, 'Esquerda', d.sentido)

    carro = Carro(Direcao(), Motor())
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())

    print(carro.sentido())
    carro.virar_a_direita()
    print(carro.sentido())
    carro.virar_a_direita()
    print(carro.sentido())
    carro.virar_a_direita()
    print(carro.sentido())
    carro.virar_a_direita()
    print(carro.sentido())
    