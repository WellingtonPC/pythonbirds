class Pessoa:
    #Atributos de classe são alocados apenas uma vez na memória
    olhos = 2

    #Atributos de instância são alocados sempre que um objeto é criado
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

    lucioano.sobrenome = 'Ramalho'
    del lucioano.filhos
    lucioano.olhos = 1
    del lucioano.olhos
    print(lucioano.__dict__)
    print(joaquim.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(lucioano.olhos)
    print(joaquim.olhos)
    print(id(Pessoa.olhos), id(lucioano.olhos), id(joaquim.olhos))