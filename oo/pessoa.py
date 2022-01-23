class Pessoa:

    def __init__(self, *filhos:list, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Oi! {id(self)}'

if __name__ == '__main__':
    joaquim = Pessoa(nome='Joaquim')
    lucioano = Pessoa(joaquim, nome='Luciano')
    print(Pessoa.cumprimentar(lucioano))
    print(id(lucioano))
    print(lucioano.cumprimentar())
    print(lucioano.nome)
    for filho in lucioano.filhos:
        print(f'Filho: {filho.nome}')