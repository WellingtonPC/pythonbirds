class Pessoa:

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


    def cumprimentar(self):
        return f'Oi! {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Joaquim'
    print(p.nome)
    print(p.idade)