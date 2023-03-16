""""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self. altura = altura

    def envelhecer (self):
        anos = input('quantos anos deseja envelhecer?\n')
        try:
            anos = int(anos) + self.idade
        except ValueError:
            print('insira uma idade valida.')
            return
        print('sua idade atual é: '+str(anos))

    def engordar(self):
        peso = input('quantos kilos deseja engordar? \n')
        try:
            peso = int(peso) + self.peso
        except ValueError:
            print('insira um peso valido')
            return
        print('seu peso atual é '+str(peso))

    def crescer(self):
        if self.idade < 21 :
            print('sua altura atual é: ' + str(int(self.altura) + int(0.5)))       

humano = pessoa('aline', 20, 50, 155)
pessoa.crescer(humano)