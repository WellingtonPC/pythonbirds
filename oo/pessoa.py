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


    #Método de classe usando o decorator @staticmethod
    @staticmethod
    def metodo_estatico():
        return 42

    #Método de classe usando o decorator @staticmethod
    @classmethod
    def get_nome_atributos_de_classe(cls):
        return f'Nome da classe: {cls} - Olhos: {cls.olhos}'

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
    print(Pessoa.metodo_estatico(), lucioano.metodo_estatico())
    print(Pessoa.get_nome_atributos_de_classe(), lucioano.get_nome_atributos_de_classe())
